import socket
import select
import random

class Server:

    def __init__(self, ip, port):

        self.s = socket.socket()
        self.s.bind((ip, port))
        self.s.listen()
        self.users = {}
        self.conn2name = {}
        self.conn2status = {}

    def check_connection(self, timeout=0.01):
        
        readlist, _, _ = select.select([self.s], [], [], timeout)
        
        if len(readlist) != 0:
            conn, addr = self.s.accept()
            self.conn2status[conn] = 'login-select'
            conn.sendall(self.hello_message().encode())

    def handle_login(self, state, text, conn):
        if state == 'select':
            if text == '1':
                conn.sendall('enter your name >>> '.encode())
                self.conn2status[conn] = 'login-login'
            elif text == '2':
                conn.sendall('enter a name >>> '.encode())
                self.conn2status[conn] = 'login-register'
            elif text == '3':
                conn.sendall('bye\n'.encode())
                del self.conn2status[conn]
        elif state == 'login':
            name = text
            if name not in self.users:
                conn.sendall(f'user {name} not found, please try again\n'.encode())
                conn.sendall(self.hello_message().encode())
                self.conn2status[conn] = 'login-select'
            else:
                self.conn2name[conn] = name
                conn.sendall(f'welcome {name}\n'.encode())
                self.users[name]['count'] += 1
                self.conn2status[conn] = 'normal'
                conn.sendall(self.normal_message().encode())

        elif state == 'register':
            name = text
            if name in self.users:
                conn.sendall(f'name {name} is used, please use another name\n>>> '.encode())
            else:
                self.conn2name[conn] = name
                self.users[name] = {
                    'count': 1,
                }
                self.conn2status[conn] = 'normal'
                conn.sendall(f'new account is created\n'.encode())
                conn.sendall(f'welcome {name}\n'.encode())
                conn.sendall(self.normal_message().encode())


    def handle_normal(self, message, conn):
        if message == '1':
            name = self.conn2name[conn]
            times = self.users[name]['count']
            conn.sendall(f'you have login {times} times\n'.encode())
            conn.sendall(self.normal_message().encode())
        elif message == '2':
            conn.sendall('bye\n'.encode())
            del self.conn2name[conn]
            del self.conn2status[conn]

    def check_message(self, timeout=0.01):

        conn_list = list(self.conn2status.keys())
        readlist, _, _ = select.select(conn_list, [], [], timeout)
        for conn in readlist:
            state = self.conn2status[conn].split('-')
            message = conn.recv(1024).decode().strip()
            if state[0] == 'login':
                self.handle_login(state[1], message, conn)
            if state[0] == 'normal':
                self.handle_normal(message, conn)


    def hello_message(self):
        message = ''
        message += 'Hello, welcome to this example game\n'
        message += 'Select an option\n'
        message += '1. Login\n'
        message += '2. Register\n'
        message += '3. exit\n'
        message += '>>> '
        return message

    def normal_message(self):
        message = ''
        message += 'Select an option\n'
        message += '1. show login time\n'
        message += '2. exit\n'
        message += '>>> '
        return message

    def run(self):
        while True:
            self.check_connection()
            self.check_message()

if __name__ == '__main__':

    server = Server('', 12345)
    server.run()