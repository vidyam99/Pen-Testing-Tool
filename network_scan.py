from socket import *
import time
from io import StringIO
import sys

def host_discovery(target):
	old_stdout = sys.stdout
	sys.stdout = mystdout = StringIO()
	startTime = time.time()
	t_IP = gethostbyname(target)
	print ('>> Starting scan on host: ', t_IP)
	for i in range(50, 500):
	    s = socket(AF_INET, SOCK_STREAM)  
	    conn = s.connect_ex((t_IP, i))
	    if(conn == 0) :
	        print ('>> Port %d: OPEN' % (i,))
	    s.close()
	print('>> Time taken:', time.time() - startTime, ' sec(s)')
	sys.stdout = old_stdout
	return mystdout.getvalue().split('\n')