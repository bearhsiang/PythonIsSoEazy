import random
import sys

def create_number():
    c1 = chr(random.randrange(26)+ord('A'))
    c2 = chr(random.randrange(26)+ord('A'))
    num = random.randrange(1e8)

    return f'{c1}{c2}-{num:08d}'

if __name__ == '__main__':
    N = int(sys.argv[1])

    for i in range(N):
        print(create_number())