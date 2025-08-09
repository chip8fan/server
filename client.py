"""
This is the messaging app client. (Work in Progress)
"""
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((socket.gethostbyname('centralserver.local'), 8000)) # connect to centralserver
	status = s.recv(1024).decode("utf-8")
	while True:
		if status == "send":
			msg = input("Me: ").encode("utf-8")
			s.sendall(msg)
			reply = s.recv(1024).decode("utf-8")
			print(f"Them: {reply}")
		elif status == "wait":
			reply = s.recv(1024).decode("utf-8")
			print(f"Them: {reply}")
			msg = input("Me: ").encode("utf-8")
			s.sendall(msg)
		if reply == "bye":
			break
