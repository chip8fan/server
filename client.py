"""
This is the messaging app client. (Work in Progress)
"""
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((socket.gethostbyname('centralserver.local'), 8000)) # connect to centralserver
	status = s.recv(1024).decode("utf-8") # get the status
	while True:
		if status == "send": # if the client sends first
			msg = input("Me: ").encode("utf-8") # type a message
			s.sendall(msg) # send it
			reply = s.recv(1024).decode("utf-8") # wait for the reply
			print(f"Them: {reply}") # print the reply
		elif status == "wait": # if the client waits
			reply = s.recv(1024).decode("utf-8") # do in reverse order
			print(f"Them: {reply}")
			msg = input("Me: ").encode("utf-8")
			s.sendall(msg)
		if reply == "bye" or msg.decode("utf-8") == "bye": # if either side says bye
			break # end the loop
