# 첫번째 풀이
N = input()
A = list(map(int, input().split()))

number = 0
for i in A:
    count = 0
    if i==1:
        continue
    for j in range(2, i+1):
        if i%j==0:
            count+=1
    if count == 1:
        number+=1

print(number)




# 두번째 풀이
N = int(input())
A = list(map(int, input().split()))

for i in A:
    if i==1:
        N-=1
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            N-=1
            break

print(N)
