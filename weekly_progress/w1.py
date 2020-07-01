start = 0
end = 100
ans = int(input('please input the ans ('+str(start)+'~'+str(end)+'): '))
count = 0
while True:
	print('round', count)
	guess = int(input('guess a number ('+str(start)+'~'+str(end)+'): '))
	if guess > ans:
		print('lower')
		end = guess
	elif guess < ans:
		print('higher')
		start = guess
	else:
		print('hit')
		break
	count += 1
	print()

print('yes, my ans is', ans)
print('you use', count, 'round')