money = int(input())
coins = input().split()
coins = [int(i) for i in coins]
coins.sort()
coins.reverse()

ans = []

for d in coins:
    n = money//d
    ans.append('$'+str(d)+':'+str(n))
    money %= d

print(','.join(ans))