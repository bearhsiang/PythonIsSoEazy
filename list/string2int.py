s = input()
s = s.split()

l = []
for number in s:
    l.append(int(number))

print(l)

# in-line for
l = [ int(number) for number in s]
print(l)

# which is same as
l = [ int(s[i]) for i in range(len(s))]
print(l)