ans = 6

guess = int(input('guess a number: '))

while ans != guess:
	print('keep trying')
	guess = int(input('guess a number: '))

print('yes, my ans is', ans)