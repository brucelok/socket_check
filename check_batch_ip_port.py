import sys, socket
from multiprocessing import Process
'''
a simple tool that read a list of IP addresses/ports from a plaintext file
and verify the remote IP/Port connection in parallel.
example file format (comma is required as a delimiter btw IP and Port):
10.0.0.1,8443
10.0.0.2,22
syntax:
$ python check_batch_ip_port.py <text filename>
author: BruceMC_Lok@cncbinternational.com
'''
def socket_connect(ip, port):
    '''
    desc: use socket() to connect target IP and Port
    args: IP, port
    return: string
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip, int(port)))
        print('connected to ' + ip + ':' + port)
    except socket.error as msg:
        print('failed to '+ ip + ':' + port + ' ' + str(msg) +'\n')
        pass
    s.close()

if __name__ == "__main__":
    # check if argument <filename> is entered
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: $ python %s <text_filename>" % sys.argv[0])
        sys.exit(1)

    textfile = sys.argv[1]  #take filename in same directory
    # check if filename is existed
    try:
        f = open(textfile, 'r')
    except OSError as e:
        print('failed to open '+ textfile + ' ' + str(e))
        sys.exit(1)
    
    procs = []
    with f:
        for line in f:
            awk = line.split(",")
            ip = awk[0]
            port = awk[1]
            
            # instantiate process with arguments(ip, port)
            proc = Process(target=socket_connect, args=(ip, port,))
            procs.append(proc)
            proc.start()    # start multiple processes to connect socket

        for proc in procs:
            proc.join()    # recycle all processes

    print('### END OF TEST ###')
