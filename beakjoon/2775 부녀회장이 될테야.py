T = int(input())

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호

    base = list(range(1, n+1))

    for i in range(k):
        for j in range(1, n):
            base[j]+=base[j-1]

    print(base[-1])
