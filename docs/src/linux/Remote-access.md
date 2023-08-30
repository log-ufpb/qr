# ssh

**ssh** is a Linux tool which allows you to remotely access a computer, connected to the Internet, via its _internet protocol_ (IP) address. To do so, you will need a command-line interface (e.g. Linux Bash Shell, on Linux), a user account on the remote computer and its IP address, and remote access privileges.

```
ssh user_account@ip_address
example: ssh user@111.1.111.111 
```

If you need to specify the port:
```
ssh -p PORT user_account@ip_address
example: ssh -p 8022 user@111.1.111.111 
```

# scp

If you need to copy files from a remote computer to your computer or vice versa, you can use the command-line tool **scp**.

## How to copy files from a remote computer to your computer?

You will need a user account on the remote computer, its IP address, the location of the file on the remote computer, and the path where you want to save the copied file.

The command to copy a file from a remote computer is:
```
scp user_account@ip_address:source_path_to_file destination_path
example: scp user@111.1.111.111:/home/file.txt ~/destination/ 
```

## How to copy files from your computer to a remote computer?

To copy files from your computer to a remote one you will need an account on the remote computer (together with its IP address), the path where the files are located on your computer, and the path where you want the files to be copied to on the remote computer.

The command to copy a file from your computer to a remotely located one is:
```
scp /source_path_to_file user_account@ip_address:/destination_path
example: scp ~/file.txt  user@111.1.111.111:~/destination/ 
```
