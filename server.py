"""
This is a basic server for messaging on the local network. (Work in Progress)
"""

import socket
sockets = [] # list of actual sockets
addresses = [] # ip addresses (only readable by the server)
running = True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(('', 8000)) # port 8000 must be opened via sudo ufw allow 8000
	s.listen(2) # connect up to 2 clients
	for _ in range(2): # do this twice
		conn, addr = s.accept() # BLOCK until a connection happens
		if _ % 2 == 0: # is this client 1?
			conn.sendall(b'send') # then client 1 gets the first message
		else: # or is this client 2?
			conn.sendall(b'wait') # then client 2 waits for client 1 to send a message
		sockets.append(conn) # append the socket
		addresses.append(addr) # and append the ip address
	while running:
		for sock in range(len(sockets)): # get the message of each client one-by-one
			data = sockets[sock].recv(1024).decode("utf-8") # message
			print(f"{addresses[sock]}: {data}") # log message history
			if data == "bye": # if a client says bye
				running = False # after this loop ends the server is halted
			for client in sockets: # go through the list of sockets
				if client != sockets[sock]: # IF the socket is not the client that sent the message
					client.sendall(data.encode("utf-8")) # send the data to the client
