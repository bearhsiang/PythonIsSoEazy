for i in range(10):
    s = input()
    if (ord(s[0]) >= ord('a') and ord(s[0]) <= ord('z')) or (ord(s[0]) >= ord('A') and ord(s[0]) <= ord('Z')):
        print(s.capitalize())
    elif ord(s[0]) >= ord('0') and ord(s[0]) <= ord('9'):
        print(s.upper())
    else:
        print(s)
    if s == 'exit' or s == 'EXIT':
        break
