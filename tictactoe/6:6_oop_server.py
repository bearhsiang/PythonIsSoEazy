import random

class Server:

    def __init__(self, name):
        self.name = name

    def setup(self):
        print('server is setup')

    def startGame(self, player1, player2):
        print('start game')

        # create game map
        game_map = GameMap()

        # iterative get choice from player1 and player2
        while True:

            for player, sign in [(player1, 'o'), (player2, 'x')]:
                choice = player.getChoice(player, game_map)
                game_map.addsign(choice, sign)
                isWin = game_map.checkWin(sign)
                if isWin:
                    break

            break

        # send winning/lose message to player

    def send(self, message, player):
        player.recv(message)

    def terminate(self):
        print('terminated')

    def getPlayer(self):
        player = BotPlayer(random.randrange(100))
        print('get player', player.name)
        return player
    
    def run(self):
        print('server starts running')

        p1 = self.getPlayer()
        p2 = self.getPlayer()


        self.startGame(p1, p2)
        self.terminate()


class BotPlayer:

    def __init__(self, name):
        self.name = name

    def recv(self, message):
        print('player receives', message)

    def getChoice(self):
        return 1


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

#-----------------------------

if __name__ == '__main__':

    server = Server('TicTacToe')
    server.setup()
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


