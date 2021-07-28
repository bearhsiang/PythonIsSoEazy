import socket

server_ip = 'localhost'
server_port = 12345

name = input('>> input your name: ')

s = socket.socket()
s.connect((server_ip, server_port))
s.sendall(name.encode())
print(s.recv(1024).decode())
s.sendall('ok'.encode())
while True:
    text = s.recv(1024)
    if not text:
        break
    print(text.decode())
    response = input('>>> ')
    s.sendall(response.encode())

s.close()