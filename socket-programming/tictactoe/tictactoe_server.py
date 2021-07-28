import socket

s = socket.socket()

ip = ''
port = 12345

game_map = [' ']*9

def get_choice(player):
    text = create(game_map)
    while True:
        player[0].sendall(text.encode())
        response = player[0].recv(1024).decode().strip()
        if response.isnumeric():
            c = int(response)
            if c < len(game_map) and game_map[c] == ' ':
                return c

def create(game_map):
    text = ''
    for i in range(9):
        text += game_map[i]
        if i % 3 == 2:
            text += '\n'
        else:
            text += '|'
    return text

win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]

def check_win(game_map, c):
    for pattern in win_patterns:
        if game_map[pattern[0]] == c and game_map[pattern[1]] == c and game_map[pattern[2]] == c:
            return True
    return False

s.bind((ip, port))
s.listen()

p1 = s.accept()
p1_name = p1[0].recv(1024).decode()
p2 = s.accept()
p2_name = p2[0].recv(1024).decode()
p1[0].sendall(('hi '+p1_name+', game starts (you are \'O\')').encode())
p2[0].sendall(('hi '+p2_name+', game starts (you are \'X\')').encode())

p1[0].recv(1024)
p2[0].recv(1024)

while True:
    c = get_choice(p1)
    game_map[c] = 'O'
    if(check_win(game_map, 'O')):
        winner = 'p1'
        break
    c = get_choice(p2)
    game_map[c] = 'X'
    if(check_win(game_map, 'X')):
        winner = 'p2'
        break

if winner == 'p1':
    p1[0].sendall(('you win!\n'+create(game_map)).encode())
    p2[0].sendall(('you lose!\n'+create(game_map)).encode())
else:
    p2[0].sendall(('you win!\n'+create(game_map)).encode())
    p1[0].sendall(('you lose!\n'+create(game_map)).encode())

p1[0].close()
p2[0].close()