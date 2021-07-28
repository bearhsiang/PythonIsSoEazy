import socket

class SocketClient:

    def __init__(self, name):
        self.name = name
        self.socket = socket.socket()

    def connect(self, server_ip, server_port):

        self.socket.connect((server_ip, server_port))
        self.send(self.name)

    def send(self, message):

        self.socket.sendall(message.encode())

    def recv(self):

        s = self.socket.recv(1024).decode()
        return s


if __name__ == '__main__':

    client = SocketClient('Sean')
    server_ip = 'localhost'
    server_port = 12345
    client.connect(server_ip, server_port)

    while True:

        s = client.recv()
        print(s)

        # todo: 
        # condition on s

        choice = input('>>> ')
        client.send(choice)

