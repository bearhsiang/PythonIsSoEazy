import random
import json
import os

def start_game(N):
	ans = random.randrange(1, N)
	start = 0
	end = N
	guess = -1
	count = 0
	while guess != ans:
		guess = input(f"guess a number between {start} - {end}: ")
		guess = int(guess)
		if guess > start and guess < end:
			if guess > ans:
				end = guess
			else:
				start = guess
		count += 1
	return count


def print_help(name):
	print('')
	print(f"Hi {name}, What are you want to do?")
	print(f"1. start guess number")
	print(f"2. change my name")
	print(f"3. show my status")
	print(f"4. show scoreboard")
	print(f"5. save")
	print(f"6. quit")

def print_login():
	print('')
	print('\
  ____                     _   _                 \n\
 / ___|_   _  ___  ___ ___| \ | |_   _ _ __ ___  \n\
| |  _| | | |/ _ \/ __/ __|  \| | | | | \'_ ` _ \ \n\
| |_| | |_| |  __/\__ \__ \ |\  | |_| | | | | | | \n\
 \____|\__,_|\___||___/___/_| \_|\__,_|_| |_| |_| \n\
	')
	print('1. Continue as guest')
	print('2. login')
	print('3. create new account')

def load_usersdata():
	
	if os.path.exists('data.json'):
		usersdata = json.load(open('data.json', 'r'))
	else:
		usersdata = {}
	
	return usersdata

def login(usersdata):

	print_login()

	q = input('>> ')
	if q == '1':
		usersdata['guest'] = {
			'highest': -1,
			'times': 0,
		}
		return 'guest'
	elif q == '2':
		while True:
			print('what\'s your name?')
			name = input('>> ')
			if name not in usersdata:
				print(f'user {name} not found ...')
			else:
				return name

	elif q == '3':
		while True:
			print('what\'s your name?')
			name = input('>> ')
			if name in usersdata:
				print(f'user {name} already exists ...')
			else:
				usersdata[name] = {
					'highest': -1,
					'times': 0,
				}
			return name

def main_loop(name, usersdata):
	
	while True:
		
		print_help(name)
		q = input('>> ')
		
		if q == '1':
			result = start_game(10)
			usersdata[name]['times'] += 1
			print(f'Congraduate! you get {result}')
			if result < usersdata[name]['highest'] or usersdata[name]['highest'] < 0:
				print('new record!!!')
				usersdata[name]['highest'] = result

		elif q == '2':
			new_name = input('New Name: ')
			if new_name == name:
				print(f'your name is already {name}')
			elif new_name in usersdata:
				print(f'Name {new_name} already exists')
			else:
				print(f'change name {name} -> {new_name}')
				usersdata[new_name] = usersdata[name]
				del usersdata[name]
				name = new_name
		
		elif q == '3':
			
			print(f'name: {name}')
			print(f'highest: {usersdata[name]["highest"]}')
		
		elif q == '4':
			for user_name in usersdata:
				if user_name != 'guest'
				print(f'{user_name}: {usersdata[user_name]}')
		elif q == '5':
			json.dump(usersdata, open('data.json', 'w'))
		elif q == '6':
			break
		

if __name__ == '__main__':

	usersdata = load_usersdata()
	
	player = login(usersdata)

	main_loop(player, usersdata)
