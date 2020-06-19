ans = 6

while True:

	guess = int(input('guess a number: '))
	
	if guess != ans:
		print('keep trying')
	else:
		print('yes, my ans is', ans)
		break