"""
This is the messaging app client. (Work in Progress)
"""
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((socket.gethostbyname('centralserver.local'), 8000)) # connect to centralserver
	msg = input("Me: ").encode("utf-8")
	s.send(msg)
	reply = b"Them: "
	while True:
		data = s.recv(1024)
		if not data:
			break
		reply = reply + data
	print(reply)
