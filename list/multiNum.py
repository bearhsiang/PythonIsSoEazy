l = []

for i in range(3):
	s = input('input some numbers (separate by space): ').split()
	for num in s:
		num = int(num)
		if num < 0 or num % 3 == 0:
			l.append(num)
l.sort()
l.reverse()
for num in l:
	print(num)
