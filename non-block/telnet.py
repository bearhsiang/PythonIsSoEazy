import socket
import select
import sys
import select

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('telnet.py [ip] [port]')

    s = socket.socket()
    s.connect((sys.argv[1], int(sys.argv[2])))

    while True:

        readlist, _, _ = select.select([s], [], [], 0.01)

        for src in readlist:

            if src == s:

                text = s.recv(1024).decode()
                print(text)


        text = input()
        s.sendall(text.encode())


