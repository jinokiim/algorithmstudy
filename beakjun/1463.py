# 틀린 풀이
X = int(input())
counter = 0

while X > 1:
    if X%3==0:
        X = X//3
        counter+=1
    elif X%2==0:
        X = X//2
        counter+=1
    else:
        X-=1
        counter+=1

print(counter)


# 틀린풀이 2
n = int(input())
d = [0]*1000001   # 최대숫자만큼 0으로 배열을 채운다.
d[1]=0
d[2]=1      # 미리 알고있는 값을 채우고,
d[3]=1      # 값을 호출하면 바로나올수 있게하여
d[4]=2      # 연산시간을 단축

for i in range(5, n+1):
    d[i] = d[i-1] + 1  # i-1 의 값 계산, 아래에서 %3이나 %2 가작으면 대체
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    elif i%2==0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])

