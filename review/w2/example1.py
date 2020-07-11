for i in range(26):
    for j in range(26):
        print(chr(ord('A')+(i+j)%26), end='')
    print()
