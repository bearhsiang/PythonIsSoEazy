while True:
    print('')
    print('\
  ____                     _   _                 \n\
 / ___|_   _  ___  ___ ___| \ | |_   _ _ __ ___  \n\
| |  _| | | |/ _ \/ __/ __|  \| | | | | \'_ ` _ \ \n\
| |_| | |_| |  __/\__ \__ \ |\  | |_| | | | | | | \n\
 \____|\__,_|\___||___/___/_| \_|\__,_|_| |_| |_| \n\
    ')
    print('1. Start game')
    print('2. quit')

    op = input('>>> ')
    if op == '1':

        ans = int(input('please input the ans (0~100): '))
        start = 0
        end = 100
        count = 0
        while True:
            print('round', count)
            guess = int(input('guess a number ('+str(start)+'~'+str(end)+'): '))
            if guess > ans:
                print('lower')
                end = guess
            elif guess < ans:
                print('higher')
                start = guess
            else:
                print('hit')
                break
            count += 1
            print()

        print('yes, my ans is', ans)
        print('you use', count, 'round')

    if op == '2':
        break