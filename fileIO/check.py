import sys
def load_number(filename):

    f = open(number_file, 'r')

    f.readline()
    special = f.readline().strip()
    f.readline()
    grand = f.readline().strip()
    f.readline()

    first = []
    for i in range(3):
        first.append(f.readline().strip())

    f.readline()
    
    additional = []
    for i in range(2):
        additional.append(f.readline().strip())

    return special, grand, first, additional


number_file = 'winning_number.txt'

special, grand, first, additional = load_number(number_file)

receipt_numbers_file = sys.argv[1]

f_in = open(receipt_numbers_file, 'r')

total = 0

for line in f_in:
    line = line.strip()
    number = line.split('-')[1]
    
    # check special price
    if number == special:
        total += 10000000
        print(f"[Special]: {line}, $10000000")
    if number == grand:
        total += 2000000
        print(f"[Grand]: {line}, $2000000")
    for first_num in first:
        if number == first_num:
            total += 200000
            print(f"[First]: {line}, $200000")
        elif number[1:] == first_num[1:]:
            total += 40000
            print(f"[Second]: {line}, $40000")
        elif number[2:] == first_num[2:]:
            total += 10000
            print(f"[Third]: {line}, $10000")
        elif number[3:] == first_num[3:]:
            total += 4000
            print(f"[Fourth]: {line}, $4000")
        elif number[4:] == first_num[4:]:
            total += 1000
            print(f"[Fifth]: {line}, $1000")
        elif number[5:] == first_num[5:]:
            total += 200
            print(f"[Sixth]: {line}, $200")
    for add_num in additional:
        if number[-3:] == add_num:
            total += 200
            print(f'[Addtional]: {line}, $200')

f_in.close()

print(f'total winnings: {total}')

