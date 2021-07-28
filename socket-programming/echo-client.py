import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 10003

s.connect((server_ip, server_port))

while True:
    message = input("> ")
    s.sendall(message.encode())
    if message == 'close':
        break
    data = s.recv(1024)

s.close()