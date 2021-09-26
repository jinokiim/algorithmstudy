T = int(input())

for i in range(T):
    S, R = input().split()
    for j in R:
        print(int(S)*j, end='')
    print()
