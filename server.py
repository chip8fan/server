"""
This is a basic server for messaging on the local network. (Work in Progress)
"""

import socket
clients = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(('', 8000)) # port 8000 must be opened via sudo ufw allow 8000
	s.listen(2) # connect up to 2 clients
	conn, addr = s.accept()
	clients.append(addr)
	s.sendall(b'Hello')
print(clients)
