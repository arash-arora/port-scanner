#!bin/python3

import sys
import socket
from datetime import datetime

#Defining our target

if len(sys.argv) == 2: #as we have 2 arguments ( scanner.py ip_addr )
	#sys.argv[0] -> scanner.py ____________ sys.argv[1] -> ip_addr
	
	target = socket.gethostbyname(sys.argv[1]) #translating hostname to ipv4

else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
	
	

#Adding a banner

print("-" * 50)
print("Scanning Target " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try :
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#AF_INET -> IPv4 ---------- SOCK_STREAM -> port
		socket.setdefaulttimeout(1) #will try connecting to a specific port for 1 sec 
		result = s.connect_ex((target, port))  #returns an error indicator -> 0 = open & 1 = not open
		if (result == 0):
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
	
except socket.gaierror: 
	print("Hostname could not be resolved.")
	sys.exit() #clean exit from all the process 
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
	
	
#python3 scanner.py <ip>

#TO make it robust and fast we can use threading so that multiple processes can be executed at once 
