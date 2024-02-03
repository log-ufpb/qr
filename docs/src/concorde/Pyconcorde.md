# PyConcorde

## Concorde Solver

The [Concorde solver](https://www.math.uwaterloo.ca/tsp/concorde.html) is a state-of-the-art algorithm for efficiently solving the symmetric [Travelling Salesman Problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem).


## Python Wrapper

A convenient way to use this solver is through the [PyConcorde](https://github.com/jvkersch/pyconcorde?tab=readme-ov-file) library, a Python wrapper that interfaces with Concorde.


### Installation

Installation instructions are well-described in the [PyConcorde Documentation](https://github.com/jvkersch/pyconcorde?tab=readme-ov-file).

### Loading a TSP problem

To load a TSP problem into the solver, provide a [TSP instance file](https://tsplib95.readthedocs.io/en/stable/). In this example, an existing instance, `a280.tsp`, is passed to the solver.

```
from concorde.tsp import TSPSolver

INSTANCE_PATH = "./a280.tsp"

solver = TSPSolver.from_tspfile(INSTANCE_PATH)
```

If you only have the distance matrix, create a TSP instance file using the [TSPLIB 95](https://tsplib95.readthedocs.io/en/stable/) library.

```
import tsplib95

distance_matrix = [
    [0, 4, 6, 9, 7],
    [4, 0, 3, 2, 2],
    [6, 3, 0, 1, 8],
    [9, 2, 1, 0, 4],
    [7, 2, 8, 4, 0]
]

SIZE = len(distance_matrix)

problem = tsplib95.models.StandardProblem()

problem.name = "example"
problem.type = "TSP"
problem.dimension = SIZE
problem.edge_weight_type = "EXPLICIT"
problem.edge_weight_format = "FULL_MATRIX"
problem.edge_weights = distance_matrix

problem.save("example.tsp")
```

To generate instances with alternative edge weight types such as EUC_2D or GEO, you can create TSP files by referring to the following [examples](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/).

### Solving

To execute the algorithm, call the `.solve()` method:

```
solution = solver.solve()
```

By default, the solver prints detailed information during execution. To disable verbosity, use the verbose parameter:

```
solution = solver.solve(verbose=False)
```

After execution, the solver returns an object containing, among others, the runtime and the computed tour, as well as flags indicating if the solve was successful and if the time bound was reached.

```
def print_solution(solution):
    print(f"Success: {solution.success}")
    print(f"Hit timebound: {solution.hit_timebound}")
    print(f"Optimal value: {solution.optimal_value} ")
    print(f"Tour: {solution.tour}")
```