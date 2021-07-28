import socket

s = socket.socket()

server_ip = 'localhost'
server_port = 12345

s.connect((server_ip, server_port))

s.sendall("this is a message from client".encode())

s.close()
