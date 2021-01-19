while True:

    print('')
    print('  ____                     _   _                  ')
    print(' / ___|_   _  ___  ___ ___| \ | |_   _ _ __ ___   ')
    print('| |  _| | | |/ _ \/ __/ __|  \| | | | | \'_ ` _ \ ')
    print('| |_| | |_| |  __/\__ \__ \ |\  | |_| | | | | | | ')
    print(' \____|\__,_|\___||___/___/_| \_|\__,_|_| |_| |_| ')
    print('1. Start game')
    print('2. quit')

    op = input('>>> ')
    if op == '1':

        ans = int(input('please input the ans (0~100): '))

        start = 0
        end = 100
        count = 1
        while True:
            print('round', count)
            guess = int(input('guess a number ('+str(start)+'~'+str(end)+'): '))
            if guess > ans:
                print('please lower!')
                end = guess
            elif guess < ans:
                print('please higher!')
                start = guess
            else:
                print('you hit the answer!')
                break
            count += 1
            print()

        print('you use', count, 'round!')

    if op == '2':
        break