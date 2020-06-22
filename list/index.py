l = ['a', 123, 'sorry', 3.14, 'other', 22]

for i in range(len(l)):
    print('l[', i, '] = ', l[i], sep='')

for i in range(-1, -len(l)-1, -1):
    print('l[', i, '] = ', l[i], sep='')
