# Existing methods

CPLEX's own documentation has some pages dedicated to
[Running out of memory](https://www.ibm.com/docs/en/icos/22.1.1?topic=problems-running-out-memory)
and to [Lack of memory](https://www.ibm.com/docs/en/icos/22.1.1?topic=problems-lack-memory).
Unfortunately these solutions DO NOT ABORT the solving procedure when the process
reaches a certain memory threshold. That means we must do it ourselves.

# DIY method
To set a memory limit and abort the solver when it exceeds said limit we will be
using:
1. A function to track the memory use of the current process
2. A CPLEX callback that will abort the process if the memory exceeds the limit.

## Tracking memory

As of yet, CPLEX doesn't have a parameter or function that returns neither the
current memory usage nor the max memory used since start.
So we provide below a C++ function that returns the current memory usage of the
current process. It works for both Linux and macOS.

```c++
#if defined(__APPLE__) && defined(__MACH__)
#include <mach/mach.h>

namespace {
size_t get_mem_usage()
{
    task_t self = mach_task_self();
    mach_task_basic_info info = {};
    mach_msg_type_number_t info_count = MACH_TASK_BASIC_INFO_COUNT;
    int ret = task_info(
        self, MACH_TASK_BASIC_INFO, reinterpret_cast<task_info_t>(&info),
        &info_count
    );

    if (ret != KERN_SUCCESS) {
        return 0;
    }

    return info.resident_size;
}
} // namespace
#elif defined(__linux__)
#include <iomanip>
#include <unistd.h>

namespace {
size_t get_mem_usage()
{
    size_t tmp = 0;
    size_t resident_size = 0;

    std::ifstream stream("/proc/self/statm");
    if (!stream.is_open()) {
        return 0;
    }
    stream >> tmp >> resident_size;

    const size_t pagesize = getpagesize();

    return resident_size * pagesize;
}
} // namespace
#endif
```

With it, we can use a `GenericClass` that updates the max memory usage
(in 500ms intervals) while CPLEX is solving an instance.

```c++
class GenericClass {
    void start_tracking_memory();
    void stop_tracking_memory();
    void memory_track_loop();

    double max_mem_used{0.0};
    double mem_limit_gb{32.0};
    bool finished{false};
};

void GenericClass::start_tracking_memory()
{
    const auto default_id = std::thread::id();
    if (thread.get_id() != default_id) {
        return;
    }

    thread = std::thread(&GenericClass::memory_track_loop, this);
}

void GenericClass::stop_tracking_memory()
{
    const auto default_id = std::thread::id();
    if (thread.get_id() == default_id) {
        return;
    }

    if (thread.joinable()) {
        thread.join();
    }
}

void GenericClass::memory_track_loop()
{
    while (!this->finished) {
        const size_t resident_size = get_mem_usage();
        const double rsize_gb = static_cast<double>(resident_size) / 1.e9;

        this->max_mem_used =
            std::max(rsize_gb, this->max_mem_used);

        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}

void GenericClass::optimize()
{
    this->finished = false;
    start_tracking_memory();
    call_solver();
    this->finished = true;
    stop_tracking_memory();
}
```

## Aborting CPLEX with callbacks
Given the class in the previous section and that it is currently tracking
the memory usage, all that is left is to define and use a callback to abort
CPLEX when the max memory used surpasses the stipulated limit.

```c++
class OOMKiller : public IloCplex::ControlCallbackI {
  public:
    GenericClass *gen_class;
    OOMKiller(IloEnv env, GenericClass *gen_class)
        : IloCplex::ControlCallbackI(env), gen_class(gen_class)
    {
    }

    IloCplex::CallbackI *duplicateCallback() const override
    {
        return new OOMKiller{*this};
    }

    void main() override
    {
        if (gen_class->max_mem_used > gen_class->mem_limit_gb) {
            abort();
        }
    }
};
```

And now to bind the callback before solving:
```c++
void GenericClass::call_solver()
{
    IloCplex solver;

    if (this->mem_limit_gb > 0.0) {
        solver.use(new OOMKiller(solver.getEnv(), this));
    }

    try {
        solver->solve();
    } catch (IloException &ex) {
        std::cerr << preamble << " Error:\n";
        ex.print(std::cerr);
    } catch (...) {
        std::cerr << preamble << " Error: Unknown exception caught!\n";
    }
}
```
