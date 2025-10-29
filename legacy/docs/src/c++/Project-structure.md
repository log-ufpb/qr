There are several ways to organize the file structure of a C++ project, and it can be confusing to find the "best" one. The reality is that there isn’t a definitive answer, as C++ lacks strong predefined standards in this area, making it somewhat subjective.

Here, we’ll recommend a solid project structure to save you time searching.

## General file and directory naming convetions

Before we start, as we will be setting up files and directories, it is important to define some naming convetions. Follow these naming guidelines to improve readability and portability:

* Avoid spaces and special characters.
* Keep names concise (under 32 characters).
* Use lowercase letters and separate words with underscores (_).

Some examples:

* `tsp_solver` ✅
* `TSP Solver` ❌

For more naming tips, check [this guide](https://resources.ascented.com/ascent-blog/tips-file-and-folder-naming-convention).

## Root directory

First, create the root directory for your project, which will contain all subdirectories and files:


```
mkdir <project_name>
cd <project_name>
```

(Optional) Adding a `README.md` at this stage is recommended. It should briefly describe your project and provide setup instructions.

```
touch README.md
```

## Source directory 

Next, create a source directory to hold your C++ source files. Usually we name this directory `src` or `source`, and both are okay, but we are going to use `src`:

```
mkdir src
cd src
```

Once we have our source directory, we have to create source files. C++ source files often use the `.cpp` suffix, though other options like `.cc`, `.C` and [others](https://gcc.gnu.org/onlinedocs/gcc-4.4.1/gcc/Overall-Options.html#index-file-name-suffix-71) exist. We’ll stick with `.cpp` as it’s the most widely recognized.

With that, we can create the main source file, typically `main.cpp`, which contains the `main()` function, that is the entry point for your program:

```
touch main.cpp
```

We're also going to create a `fool.cpp` just to exemplify other source files:

```
touch fool.cpp
```

## Include directory

When working with multiple files in C++, probably you will need to create some header files. We are going to store those files in the `include` directory:

```
cd ..
mkdir include
cd include
```

Then, we can create our header files. Note that, just like the source files, there are some different possible file sufixes (`.h`, `.hpp`, [etc](https://gcc.gnu.org/onlinedocs/gcc-4.4.1/gcc/Overall-Options.html#index-file-name-suffix-71)). `.hpp` is preferred here to clearly indicate C++ header files (as `.h` is also used in C)

```
touch foo.hpp
```

## Initialize git (optional)

Even though using git is not exactly C++, it is recommended to always use it. 

```
cd ..
git init
```

This will create a `.git` directory.

Next, create a `.gitignore` file to specify which files Git should ignore. Typically, compiled binaries and object files are excluded:

```
touch .gitignore
```

For a C++ `.gitignore` template, see [GitHub's C++ gitignore](https://github.com/github/gitignore/blob/main/C%2B%2B.gitignore)

## Final structure

The final structure of our generic C++ project is pretty simple (`foo.cpp` and `foo.hpp` are just for the example).

```
cd ..
tree -a <project_name>
```

And it should return (we abstracted the things inside the `.git` directory, because they are not relevant now):

```
<project_name>
├── .git
├── .gitignore
├── include
│   └── foo.hpp
├── README.md
└── src
    ├── foo.cpp
    └── main.cpp
```

## Automation 

Although the project structure is straightforward and could be built quickly by executing each step as we did, it's even better to streamline this setup with a single, automated command. This reduces the risk of errors that might arise 
and saves you some time from running 6-10 separate commands manually.

To simplify this process, we recommend creating a [shell script](https://en.wikipedia.org/wiki/Shell_script) that automates everything in one go. You can find a simple script for this project structure [here](https://github.com/guidantas21/cpp-programming/tree/main/project_structure).