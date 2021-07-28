class BotPlayer:

    def __init__(self, name):
        self.name = name

    def recv(self, message):
        print('player receives')
        print(message)

    def send(self):
        # s = input().strip()
        # return s
        return str(random.randrange(9))

class CommandlinePlayer:

    def __init__(self, name):
        self.name = name

    def recv(self, message):
        print('you receive')
        print(message)

    def send(self):

        s = input(">>> your choice: ").strip()

        return s

class SocketPlayer:

    def __init__(self, conn):
        self.conn = conn

    def send(self):
        s = self.conn.recv(1024).decode()
        return s

    def recv(self, message):
        self.conn.sendall(message.encode())