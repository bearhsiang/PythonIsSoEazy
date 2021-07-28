import socket
import select
import random

s = socket.socket()
ip, port = '', 12345
s.bind((ip, port))
s.listen()

timeout = 0.001

connect_list =[]
id2name = {}
name2id = {}
id2connect = {}

while True:

    accept_list, _, _ = select.select([s], [], [], timeout)

    if len(accept_list) != 0:
        conn, addr = s.accept()
        connect_list.append(conn)
        default_name = f'User{random.randrange(10000)}'
        id2name[conn.fileno()] = default_name
        name2id[default_name] = conn.fileno()
        id2connect[conn.fileno()] = conn

    read_list, _, _ = select.select(connect_list, [], [], 0.001)

    for read_conn in read_list:
        message = read_conn.recv(1024).decode().strip()
        message = message.split()
        if message[0] == 'broadcast':
            text = ' '.join(message[1:])
            for conn in connect_list:
                conn.sendall(f'[broadcast] {id2name[read_conn.fileno()]}: {text}\n'.encode())

        if message[0] == 'name':
            name = ' '.join(message[1:])
            id2name[read_conn.fileno()] = name
            name2id[name] = read_conn.fileno()
            read_conn.sendall(f'[info] set name to "{name}"\n'.encode())
        
        if message[0] == 'exit':
            read_conn.close()
            connect_list.remove(read_conn)

        if message[0] == 'private':
            name = message[1]
            text = ' '.join(message[2:])
            sender = id2name[read_conn.fileno()]
            id2connect[name2id[name]].sendall(f'[private] {sender}: {text}\n'.encode())

        if message[0] == 'myname':
            name = id2name[read_conn.fileno()]
            read_conn.sendall(f'[info] {name}\n'.encode())

