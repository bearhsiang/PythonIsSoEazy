s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = input().split()
output = []

for num in l:
	output.append(s[int(num)])

print(''.join(output))