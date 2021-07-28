import select
import socket

if __name__ == '__main__':

    s = socket.socket()
    ip = ''
    port = 12345
    s.bind((ip, port))
    s.listen()

    timeout = 1
    counter = 0

    s_list = []

    while True:

        print(' '*20, end='\r')
        print('waiting', '.'*(counter%3), end='\r')

        connect_list, _, _ = select.select([s], [], [], timeout)

        if len(connect_list) != 0:
            s_list.append(s.accept()[0])

        read_list, _, _ = select.select(s_list, [], [], 0)

        for read_s in read_list:
            text = read_s.recv(1024).decode()
            read_s.sendall(text.encode())


        counter += 1