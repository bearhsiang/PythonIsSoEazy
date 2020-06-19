ans = 6

while True:

	guess = int(input('guess a number: '))

	if guess > ans:
		print('lower')
	elif guess < ans:
		print('higher')
	else:
		print('hit')
		break