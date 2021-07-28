import random
import socket

class Server:

    def __init__(self, name):
        self.name = name

    def setup(self, ip, port):
        self.socket = socket.socket()
        self.socket.bind((ip, port))
        self.socket.listen()
        print('server is setup')

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
            # print('winner name is', player_dict[winner].name)
            loser = 'o' if winner == 'x' else 'x'
            player_dict[winner].recv('you win')
            player_dict[loser].recv('you lose')
        else:
            # print('tie!!!')
            player1.recv('tie!')
            player2.recv('tie!')
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
        p = SocketPlayer(conn)
        name = p.send()
        p.name = name
        return p
    
    def run(self):
        print('server starts running')

        # p1 = self.getPlayer()
        # p1 = CommandlinePlayer('hah')
        p1 = AIPlayer('bot', 'o')
        # p2 = self.getPlayer()
        p2 = CommandlinePlayer('sean(CommandLine)')

        self.startGame(p1, p2)
        self.terminate()

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

class AIPlayer:

    win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def recv(self, message):
        if message[:5] == '[MAP]':
            game_map = self.parse_map(message)
            self.status = game_map
            print(self.status)

    def parse_map(self, map_string):
        map_string = map_string.replace('[MAP]', '')
        map_string = map_string.replace('\n', '')
        map_string = map_string.replace('|', '')
        return list(map_string)
    
    def send(self):

        opponent  = 'x' if self.sign == 'o' else 'o'
        for pattern in self.win_patterns:

            p0 = self.status[pattern[0]]
            p1 = self.status[pattern[1]]
            p2 = self.status[pattern[2]]

            if p0 == opponent and p1 == opponent and p2 == ' ':
                return str(pattern[2])

            if p0 == opponent and p1 == ' ' and p2 == opponent:
                return str(pattern[1])

            if p0 == ' ' and p1 == opponent and p2 == opponent:
                return str(pattern[0])

        if self.status[4] == ' ':
            return str(4)

        return str(random.randrange(9))


class SocketPlayer:

    def __init__(self, conn):
        self.conn = conn

    def send(self):
        s = self.conn.recv(1024).decode()
        return s

    def recv(self, message):
        self.conn.sendall(message.encode())


class GameMap:

    win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]

    def __init__(self):
        self.game_map = [' ']*9

    def to_text(self):
        m = '[MAP]\n'
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


    # Unit test for GameMap
    # input a list of choice, check our code is worked
    # gameMap = GameMap()
    # for i in range(10):
    #     print(gameMap.to_text())
    #     choice = input('>>your choice: ')
    #     if gameMap.isValid(choice):
    #         gameMap.addsign(choice, 'o')
    #     else:
    #         print('the choice', choice, 'is invalid')
    #     if gameMap.checkWin('o'):
    #         print('you win')
    #         break
