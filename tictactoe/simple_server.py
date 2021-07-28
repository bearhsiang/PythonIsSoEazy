import socket

s = socket.socket()

ip = 'localhost'
port = 12345

s.bind((ip, port))
s.listen()

# ---------
conn, addr = s.accept()

message = conn.recv(1024).decode()
print(message)

s.close()