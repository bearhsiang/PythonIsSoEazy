change = input()
change = int(change)

amount = change // 53
print('53:', amount)
change %= 53
amount = change // 33
print('33:', amount)
change %= 33
print('1:', change)
