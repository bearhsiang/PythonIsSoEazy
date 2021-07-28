import socket

class SocketPlayer:

    def __init__(self, name):
        self.socket = socket.socket()
        self.name = name

    def connect(self, server_ip, server_port):
        self.socket.connect((server_ip, server_port))
        self.send(self.name)

    def recv(self):
        s = self.socket.recv(1024).decode()
        return s

    def send(self, message):
        self.socket.sendall(message.encode())

if __name__ == '__main__':

    player = SocketPlayer('sean')
    server_ip = 'localhost'
    server_port = 12345
    player.connect(server_ip, server_port)
    
    while True:
        print(player.recv())
        s = input(">>> ")
        player.send(s)