print('while version:')
sum = 0
i = 1

while i <= 100:
	sum += i
	i += 1

print('sum is', sum)
print()

print('for version:')
sum = 0

for i in range(101):
	sum += i

print('sum is', sum)