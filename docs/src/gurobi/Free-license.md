## Retrieving a license

To retrieve a Gurobi _named-user academic_  license, please refer to the [Quick Start](https://www.gurobi.com/wp-content/plugins/hd_documentations/documentation/10.0/quickstart_linux.pdf#page=10) guide. This type of license is designed for a single person, on a single machine.

You must be connected to an academic domain to request a new _named-user academic_ license, otherwise, an `Academic Domain Error` will be issued. In the case of UFPB, a workaround to this issue can be found in [How to access academic portals from outside UFPB's network domain](../hacks/Access-academic-portals).

## Setting up a license

Assuming the license has been downloaded to the `home` directory, i.e., `home/<user>`.

1. Rename the license file.
```
$ mv gurobi.lic $HOSTNAME
```

1. Add the following line to the `.bashrc` file.
```
export GRB_LICENSE_FILE="/home/<user>/$HOSTNAME"
```

These steps are especially important for users with a `home` folder shared among multiple machines. For example, assume the user `log` has a `home` directory shared between machines q1 and q2, and each machine has a Gurobi installation (see [Shared installation](shared-installation)). In such case, downloading and exporting the GRB_LICENSE_FILE as in the aforementioned steps, for both machines, lets Gurobi select the corresponding license file according to the machine you are logged in.

Do not forget to `source` the modified `.bashrc` file, or reboot the machine, for changes to take effect.
```
$ source .bashrc
```