#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500               # Reserve a port for your service.

s.connect((host, port))
s.sendall(str.encode(input('Enter Greeting: ')))
data = s.recv(1024)
print(data.decode("utf-8"))
#print(s.recv(1024).decode("utf-8"))
s.close()