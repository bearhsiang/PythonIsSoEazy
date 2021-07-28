import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 10003

s.bind((ip, port))
s.listen()

for i in range(3):
    conn, addr = s.accept()
    while True:
        raw = conn.recv(2014)
        raw = raw.decode().strip()
        print(raw)
        if raw == 'close':
            break
        conn.sendall(raw.encode())

    conn.close()

s.close()
