# socket_check
The python script to verify connection to target IP and Port

### run in batch
Prepare the list of IPs and Ports in a plaintext file
```
192.168.12.13,22
www.google.com 443
```
run check_batch_ip_port.py
```
$ python check_batch_ip_port.py <list_of_ip_port_in_plaintext_file>
```
Sample output
```
$ python check_batch_ip_port.py ls_example
connected to 10.70.59.89:8443

failed to 10.70.59.90:8443
[WinError 10061] No connection could be made because the target machine actively refused it

connected to 10.70.61.89:8080

connected to 10.70.61.90:8090

connected to www.cncbinternational.com:80

failed to www.google.com:443 timed out

### END OF TEST ###
```

### run single socket
run check_ip_port.py for single IP and Port
```
$ python check_ip_port.py 127.0.0.1 53
```