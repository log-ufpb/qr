# Remote access

The _secure shell_ (SSH) is a protocol for secure remote login and other secure network operations over insecure networks, as suggested by the [RFC 4251](https://datatracker.ietf.org/doc/html/rfc4251). ssh is an open-source implementation of such protocol. To securely connect and log into a destination machine using ssh, you will need a command-line interface (e.g. Linux Bash Shell, on Linux), a user account on the remote computer and the hostname or _internet protocol_ (IP) address of such host.

```
ssh user_account@ip_address
example: ssh user@111.1.111.111 
```

If you need to specify the port:
```
ssh -p PORT user_account@ip_address
example: ssh -p 8022 user@111.1.111.111 
```

# File transfer

If you need to copy files from a remote host to your computer or vice versa, you can use the command-line tool scp.

## How to copy files from a remote computer to your machine?

You will need a user account on the remote host, the hostname or IP address of the machine, the location of the file, and the path where you want to save the copied file.

```
scp user_account@ip_address:source_path_to_file destination_path
example: scp user@111.1.111.111:/home/file.txt ~/destination/ 
```

## How to copy files from your machine to a remote host?

To copy files from your computer to a remote one you will need an account on the remote machine, the hostname, the path where the file is located on your computer, and the path where you want the file to be copied to on the remote host.

```
scp /source_path_to_file user_account@ip_address:/destination_path
example: scp ~/file.txt  user@111.1.111.111:~/destination/ 
```
