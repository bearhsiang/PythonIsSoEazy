import select
import socket



if __name__ == '__main__':

    # server setup
    s = socket.socket()
    ip, port = '', 12346
    s.bind((ip, port))
    s.listen()
    connect_list = []

    while True:

        # new connection
        incoming_list, _, _ = select.select([s], [], [], 0.01)

        if len(incoming_list) > 0:
            conn, addr = s.accept()
            connect_list.append(conn)

        # data 
        if len(connect_list) > 0:

            read_list, _, _ = select.select(connect_list, [], [], 1)

            for conn in read_list:

                text = conn.recv(1024).decode().strip()
                text = text.split()

                command = text[0]

                # broadcast
                if command == 'broadcast':
                    for user in connect_list:
                        message = '[broadcast] ' + ' '.join(text[1:])
                        user.sendall(message.encode())


