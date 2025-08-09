"""
This is a basic server for messaging on the local network. (Work in Progress)
"""

import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(('', 8000)) # port 8000 must be opened via sudo ufw allow 8000
	s.listen(2) # connect up to 2 clients
	conn1, addr1 = s.accept() # this is BLOCKING, waits for the 1st connection
	conn2, addr2 = s.accept() # this is BLOCKING, waits for the 2nd connection
	while True:
		data = conn1.recv(1024)
		conn2.sendall(data)
		data = conn2.recv(1024)
		conn1.sendall(data)

