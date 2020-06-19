print('continue version:')

N = 10
i = 0

while i < N:

	if i == 5:
		i += 1
		continue

	print(i)
	i += 1

print()

print('break version:')

N = 10
i = 0

while i < N:

	if i == 5:
		i += 1
		break

	print(i)
	i += 1

print()