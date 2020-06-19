ans = 6

for i in range(10):
	print('round', i)
	guess = int(input('guess a number: '))
	if guess != ans:
		print('keep trying')
	else:
		print('yes, my ans is', ans)