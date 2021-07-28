import socket 

class Player:

    def __init__(self, name, conn, addr):
        self.name = name
        self.s = conn
        self.addr = addr

    def send(self, text, ack=True):
        self.s.sendall(text.encode())
        if ack:
            self.recv(ack=False)

    def recv(self, ack=True):
        text = self.s.recv(1024).decode().strip()
        if ack == False:
            self.send('ack', ack=False)
        return text

    def terminate(self):
        self.s.close()

class Map:

    win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]

    def __init__(self):
        self.game_map = ["_"] * 9

    def toString(self):
        text = ''
        for i in range(9):
            text += self.game_map[i]
            if i % 3 == 2:
                text += '\n'
            else:
                text += '|'
        return text

    def check_win(self):
        pass

    def is_valid(self, pos):
        if pos.isnumeric():
            pos = int(pos)
            if pos < 0 or pos > 8:
                return False
            else:
                return self.game_map[pos] == '_'
        return False

    def choose(self, pos, sign):
        self.game_map[pos] = sign

class Server:

    def __init__(self, name):

        self.name = name
        self.s = None

    def setup(self, ip, port):
        self.s = socket.socket()
        self.s.bind((ip, port))
        self.s.listen()

    def getPlayer(self):
        conn, addr = self.s.accept()
        name = conn.recv(1024).decode().strip()
        p = Player(name, conn, addr)
        return p

    def getChoice(self, player, game_map):
        while True:
            player.send(game_map.toString())
            c = player.recv()
            if game_map.is_valid(c):
                break
        
        return int(c)


    def startGame(self):
        print('Game start!!!')
        game_map = Map()
        p1 = self.getPlayer()
        p2 = self.getPlayer()
    
        p1.send("game start!!! you are the 'O'")
        p2.send("game start!!! you are the 'X'")

        winner = None
        loser = None

        while True:
            c = self.getChoice(p1, game_map)
            game_map.choose(c, 'O')
            if game_map.check_win():
                winner = p1
                loser = p2
                break
            c = self.getChoice(p2, game_map)
            game_map.choose(c, 'X')
            if game_map.check_win():
                winner = p2
                loser = p1
                break

        winner.send("you win")
        loser.send("you lose")

        p1.terminate()
        p2.terminate()

    def terminate(self):
        if self.s is not None:
            self.s.close()
            self.s = None

    def run(self, port, ip):

        self.setup(port, ip)
        self.startGame()
        self.terminate()

if __name__ == '__main__':

    ip = ''
    port = 12345

    server = Server('TicTacToe')
    server.run(ip, port)

    # m = Map()

    # m.choose(4, 'X')

    # print(m.is_valid('dsa'))
    # print(m.toString())
