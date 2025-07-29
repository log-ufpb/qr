Please, follow the instructions on the [quick start](https://www.gurobi.com/wp-content/plugins/hd_documentations/documentation/10.0/quickstart_linux.pdf#page=7) guide for a shared installation. Then, add the following lines to the `/etc/profile` file.
```
export GUROBI_HOME="/opt/gurobi1003/linux64"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"
```