#!/usr/bin/env python3
from time import sleep
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9500        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Waiting for a connection...')
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            elif data == b"Hello":
                reply = b"Hi"
            else:
                reply = b'Goodbye'
            conn.sendall(reply)
            sleep(1)
#conn.close()