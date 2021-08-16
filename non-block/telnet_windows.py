import socket
import select
import sys
import msvcrt

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('telnet.py [ip] [port]')

    s = socket.socket()
    s.connect((sys.argv[1], int(sys.argv[2])))

    buf = ''

    while True:

        readlist, _, _ = select.select([s], [], [], 0.01)

        for src in readlist:

            if src == s:

                text = s.recv(1024).decode()
                print(text)

        if msvcrt.kbhit():
            ch = msvcrt.getch().decode()
            if ch == '\r':
                s.sendall(buf.encode())
                buf = ''
                print()
            else:
                buf += ch

            print(ch, end='')

        # print(buf, end='\r')




