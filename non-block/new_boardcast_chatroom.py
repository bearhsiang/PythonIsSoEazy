import socket
import select
import random

s = socket.socket()
ip, port = '', 12346
s.bind((ip, port))
s.listen()

timeout = 0.001

connect_list =[]
name2conn = {}
conn2name = {}


while True:

    accept_list, _, _ = select.select([s], [], [], timeout)

    if len(accept_list) != 0:
        conn, addr = s.accept()
        connect_list.append(conn)
        default_name = f'User{random.randrange(10000)}'
        name2conn[default_name] = conn
        conn2name[conn] = default_name

    read_list, _, _ = select.select(connect_list, [], [], 0.001)

    for read_conn in read_list:
        message = read_conn.recv(1024).decode().strip()
        message = message.split()
        if message[0] == 'broadcast':
            text = ' '.join(message[1:])
            for conn in connect_list:
                conn.sendall(f'[broadcast] {conn2name[read_conn]}: {text}\n'.encode())

        if message[0] == 'name':
            name = ' '.join(message[1:])
            conn2name[read_conn] = name
            name2conn[name] = read_conn
            read_conn.sendall(f'[info] set name to "{name}"\n'.encode())
        
        if message[0] == 'exit':
            read_conn.close()
            connect_list.remove(read_conn)
            name = conn2name[read_conn]
            del conn2name[read_conn]
            del name2conn[name]

        if message[0] == 'private':
            name = message[1]
            text = ' '.join(message[2:])
            sender = conn2name[read_conn]
            name2conn[name].sendall(f'[private] {sender}: {text}\n'.encode())

        if message[0] == 'myname':
            name = conn2name[read_conn]
            read_conn.sendall(f'[info] {name}\n'.encode())

        if message[0] == 'list':
            users = list(name2conn.keys())
            read_conn.sendall(f"{' '.join(users)}\n".encode())
