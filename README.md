# socket_check

Run python script check_batch_ip_port.py from anyone of OpenShift worker node in each env

### run in batch
```
$ python check_batch_ip_port.py <list_of_ip_port_in plaintext_file>
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