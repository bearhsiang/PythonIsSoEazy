import random
import socket

class Server:

    def __init__(self, name):
        self.name = name

    def setup(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()
        print('server setup successfully')

    def startGame(self, player1, player2):
        print('start game')

        # create game map
        game_map = GameMap()

        is_finish = False
        winner = None

        player_dict = {
            'o': player1,
            'x': player2
        }

        # iterative get choice from player1 and player2
        while not is_finish:

            for player, sign in [(player1, 'o'), (player2, 'x')]:
                choice = self.getChoice(player, game_map)
                game_map.addsign(choice, sign)
                isWin = game_map.checkWin(sign)
                if isWin:
                    is_finish = True
                    winner = sign
                    break
                isTie = game_map.checkTie()
                if isTie:
                    is_finish = True
                    break

            # break
        print(game_map.to_text())
        print('winner is', winner)
        if winner != None:
            print('winner name is', player_dict[winner].name)
        else:
            print('tie!!!')
        # send winning/lose message to player

    def getChoice(self, player, game_map):

        while True:
            self.send(game_map.to_text(), player)
            choice = self.recv(player)
            if game_map.isValid(choice):
                break

        return choice

    def recv(self, player):
        return player.send()

    def send(self, message, player):
        player.recv(message)

    def terminate(self):
        self.socket.close()
        print('terminated')

    def getPlayer(self):
        conn, addr = self.socket.accept()
        player = SocketPlayer(conn)
        name = player.send()
        player.name = name
        return player
    
    def run(self):
        print('server starts running')

        p1 = self.getPlayer()
        p2 = self.getPlayer()
        # p2 = CommandLinePlayer('sean')


        self.startGame(p1, p2)
        self.terminate()


class SocketPlayer:

    def __init__(self, connection):
        self.conn = connection

    def recv(self, message):
        self.conn.sendall(message.encode())

    def send(self):
        s = self.conn.recv(1024).decode()
        return s
    
class BotPlayer:

    def __init__(self, name):
        self.name = name

    def recv(self, message):
        print('player receives')
        print(message)
        # pass

    def send(self):
        # s = input().strip()
        # return s
        return str(random.randrange(9))

class CommandLinePlayer:

    def __init__(self, name):
        self.name = name

    def recv(self, message):
        print('you receive:')
        print(message)

    def send(self):
        s = input("send: ")
        return s


class GameMap:

    win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]

    def __init__(self):
        self.game_map = [' ']*9

    def to_text(self):
        m = ''
        for i in range(9):
            m += self.game_map[i]
            if i % 3 == 2:
                m += '\n'
            else:
                m += '|'
        return m

    def isValid(self, choice):

        if not choice.isnumeric():
            return False

        choice = int(choice)

        if choice < 0 or choice > 8:
            return False

        if self.game_map[choice] != ' ':
            return False

        return True

    def addsign(self, choice, sign):
        choice = int(choice)
        self.game_map[choice] = sign

    def checkWin(self, c):
        for pattern in self.win_patterns:
            if self.game_map[pattern[0]] == c and self.game_map[pattern[1]] == c and self.game_map[pattern[2]] == c:
                return True
        return False

    def checkTie(self):
        
        if ' ' in self.game_map:
            return False

        return True




#-----------------------------

if __name__ == '__main__':

    server = Server('TicTacToe')
    server_ip = ''
    server_port = 12345
    server.setup(server_ip, server_port)
    server.run()

