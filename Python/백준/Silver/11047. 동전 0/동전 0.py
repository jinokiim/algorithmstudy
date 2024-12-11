n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

coins.reverse()
count = 0

for i in coins:
    count += k//i
    k %= i

    if k==0:
        break
        
print(count)