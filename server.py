"""
This is a basic server for messaging on the local network. (Work in Progress)
"""

import socket
sockets = []
running = True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(('', 8000)) # port 8000 must be opened via sudo ufw allow 8000
	s.listen(2) # connect up to 2 clients
	for _ in range(2):
		conn, addr = s.accept()
		sockets.append(conn)
	while running:
		for sock in sockets:
			data = sock.recv(1024)
			if data.decode("utf-8") == "bye":
				running = False
			for client in sockets:
				if client != sock:
					client.sendall(data)
