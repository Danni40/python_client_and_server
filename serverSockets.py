#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = c.recv(1024)
    if not data:
        break
    elif data == b"Hello":
        reply = b"Hi"
    else:
        reply = b'Goodbye'
    c.sendall(reply)
    #c.send(str.encode('Thank you for connecting'))
c.close()               # Close the connection
