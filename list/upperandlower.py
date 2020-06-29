while True:
    s = input()
    if (ord(s[0]) >= ord('a') and ord(s[0]) <= ord('m')) or (ord(s[0]) >= ord('A') and ord(s[0]) <= ord('M')):
        print(s.upper())
    elif (ord(s[0]) >= ord('n') and ord(s[0]) <= ord('z')) or (ord(s[0]) >= ord('N') and ord(s[0]) <= ord('Z')):
        print(s.lower())
    else:
        print(s)
    
    if s == 'exit' or s == 'EXIT':
        break