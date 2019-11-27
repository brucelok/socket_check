import sys, subprocess, platform
from multiprocessing import Process
'''
The script able to ping multiple ip addresses in parallel at once 
with native Python library.  simply read a list of IP from a plaintext file
example: $ python multiping.py <file_list>
author: lok.bruce@gmail.com
'''

# Global var for defining ping arg btw Windows and Linux
param = '-n' if platform.system() == 'Windows' else '-c'

def cmd_ping(ip):
    '''
    call system command 'ping' to target IP few times
    arg: IP address
    return: string
    '''
    count = '2'
    timeout = '3'
    resp = subprocess.Popen(['ping', ip, param, count, '-w', timeout], stdout=subprocess.PIPE).stdout.read()
    if str(resp).count('Request timed out') > 1:
        print('%s dead' % ip)
    else:
        print('%s live' % ip)

if __name__ == "__main__":
    #print(param)
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
        for ip in f:
            # instantiate process with arguments(ip, port)
            proc = Process(target=cmd_ping, args=(ip,))
            procs.append(proc)
            proc.start()    # start multiple processes to connect socket

        for proc in procs:
            proc.join()    # recycle all processes

    print('### END OF PING TEST ###')
