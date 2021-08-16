import socket
import select
import random

s = socket.socket()
ip, port = '', 12346
s.bind((ip, port))
s.listen()

timeout = 0.001

connect_list =[]
conn2name = {}

while True:

    # check for new connection
    accept_list, _, _ = select.select([s], [], [], timeout)

    if len(accept_list) != 0:
        conn, addr = s.accept()
        name = 'User' + str(random.randrange(10000))
        connect_list.append(conn)
        conn2name[conn] = name


    # check for data input
    if len(connect_list) == 0:
        continue

    read_list, _, _ = select.select(connect_list, [], [], 0.001)

    for read_conn in read_list:
        message = read_conn.recv(1024).decode().strip()

        message = message.split()
        
        if message[0] == 'broadcast':
            sender_name = conn2name[read_conn]
            text = ' '.join(message[1:])
            for conn in connect_list:

                conn.sendall(('[BC] '+sender_name+":"+text+'\n').encode())

        elif message[0] == 'myname':
            sender_name = conn2name[read_conn]
            read_conn.sendall(('[IF] your name is '+sender_name+'\n').encode())

        # change name
        elif message[0] == 'name':

            new_name = ' '.join(message[1:])
            conn2name[read_conn] = new_name
            read_conn.sendall(('[IF] set name to '+new_name+'\n').encode())

        elif message[0] == 'list':

            name_list = []

            for conn in connect_list:
                name = conn2name[conn]
                name_list.append(name)

            read_conn.sendall(('[IF] '+' '.join(name_list) + '\n').encode())

        elif message[0] == 'private':
            sender_name = conn2name[read_conn]
            text = ' '.join(message[1:])
            for conn in connect_list:
                if message[1] == conn2name[conn]:
                    conn.sendall(('[PM] '+sender_name+":"+text+'\n').encode())


















