# socket_check
The python script to verify multiple TCP connections in parellel.

### 1. Multi-ping
`multiping.py` is similar to Linux `ping`, but it can ping multiple hosts in parallel with multi-threading.
First prepare the list of IPs or Hostname in a plaintext file.
Then run `multiping.py` with the text file as argument
```
$ python multiping.py <file_list>
```

### 2. Check multiple sockets connections in parallel
`multinetcat.py` is similar to Linux `netcat` utility, but it can check multiple TCP connections in parallel with multi-threading.

First prepare the list of IPs and Ports in a plaintext file, e.g.
```
10.70.59.89,8443
10.70.59.90,8443
www.cncbinternational.com,80
```

Then run `multinetcat.py` with the text file as argument
```
$ python multinetcat.py ls_example
connected to 10.70.59.89:8443

failed to 10.70.59.90:8443
[WinError 10061] No connection could be made because the target machine actively refused it

connected to www.cncbinternational.com:80
### END OF TEST ###
```

### Single socket
For single socket, simply run `netcat` instead
