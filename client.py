"""
This is the messaging app client. (Work in Progress)
"""
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((socket.gethostbyname('centralserver.local'), 8000)) # connect to centralserver
	while True:
		data = s.recv(1024).decode("utf-8")
		print(f"Them: {data}")
		msg = input("Me: ").encode("utf-8")
		s.sendall(msg)
