ans = 666
count = 0
while True:
	print('round', count)
	guess = int(input("guess a number: "))
	if guess > ans:
		print('lower')
	elif guess < ans:
		print('higher')
	else:
		print('hit')
		break
	count += 1
	print()

print('yes, my ans is', ans)
print('you use', count, 'round')