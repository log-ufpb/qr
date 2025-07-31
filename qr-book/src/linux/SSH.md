The _Secure Shell_ (SSH) protocol, as defined in [RFC 4251](https://datatracker.ietf.org/doc/html/rfc4251), is a powerful tool for conducting secure remote logins and various other secure network operations, especially over potentially insecure networks. SSH is an open-source implementation of this protocol.

A cornerstone of SSH is key-based authentication, offering a significantly more secure and efficient approach compared to traditional password-based authentication. Key-based authentication utilizes a pair of cryptographic keys: a public key (used by remote servers to verify your identity) and a private key (used to prove your identity and should never be shared).

## Generating SSH keys

To generate an SSH key pair, use the `ssh-keygen` command with the recommended Ed25519 algorithm, known for its robust security features.

```
ssh-keygen -t ed25519
```

During this process, you can specify a name and destination for your keys and set a passphrase. It is advisable to save these keys in the default location (`~/.ssh/` directory) since some applications can automatically locate them. Note that you can have multiple keys, so exercise caution to avoid overwriting previously generated keys by choosing distinct names and/or destinations.

## Managing your keys

Following key generation, you will have two new files in the specified destination folder. For example, the `~/.ssh/id_ed25519.pub` file represents the public key, while the `~/.ssh/id_ed25519` file contains the private key. The public key is shared with remote servers, and the `ssh-agent` takes care of managing your private keys.

To begin, ensure that the `ssh-agent` is running in the background:

```
eval `ssh-agent`
```

Next, add your private key to the agent:

```
ssh-add /location/to/the/key
example: ssh-add ~/.ssh/id_ed25519
```

Without specifying the location, it'll automatically add all the keys from the `~/.ssh/` directory to the agent.

You can verify whether the key has been successfully added by running:

```
ssh-add -l
```

This command also displays previously added keys, if any.


# Remote access

To securely connect and log into a destination machine using ssh, you will need a user account on the remote computer and the hostname or _internet protocol_ (IP) address of such host.

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
