f = open('babyshark_lyric.txt', 'r')

# for line in f:
#     print(line)

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)

f.close()
