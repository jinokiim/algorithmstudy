# 첫번째 풀이(오답)
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    ho = (N//H+1)
    if ho < 10:
        ho = '0'+str(ho)
    else:
        ho = str(ho)
    print(floor+ho)

# 두번째 풀이

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    ho = N//H+1
    if floor==0:
        floor = H
        ho -= 1
    print(floor*100+ho)
