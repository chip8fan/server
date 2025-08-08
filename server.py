"""
This is a basic server for messaging on the local network. (Work in Progress)
"""

import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(('', 8000)) # port 8000 must be opened via sudo ufw allow 8000
	s.listen(4) # connect up to 4 clients
	conn, addr = s.accept() # this is BLOCKING
	print(addr) # placeholder

