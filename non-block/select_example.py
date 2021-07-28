import select
import socket

s = socket.socket()
ip = ''
port = 12346
s.bind((ip, port))
s.listen()

timeout = 1 # second

while True:

    rlist, _, _ = select.select([s], [], [], timeout)

    if len(rlist) != 0:
        conn, addr = s.accept()
        print(conn, addr)
        print(conn.getpeername())

    print('next')