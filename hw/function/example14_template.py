def print_opening():


def playgame(answer):

    return count # count is the number of round

while True:

    print_opening()

    op = input('>>> ')

    if op == '1':

        ans = int(input('please input the ans (0~100): '))

        count = playgame(ans)

        print('you use', count, 'round!')

    if op == '2':
        
        break