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
