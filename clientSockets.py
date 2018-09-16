#!/usr/bin/env python3
from time import sleep
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9500        # The port used by the server
connected = True
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str.encode(input('Enter Greeting: ')))
        data = s.recv(1024)

        print(repr(data.decode("utf-8")))
s.close()
