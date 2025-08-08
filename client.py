"""
This is the messaging app client. (Work in Progress)
"""
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(('centralserver.local', 8000)) # connect to centralserver
