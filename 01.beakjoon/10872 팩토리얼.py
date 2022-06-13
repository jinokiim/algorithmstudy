# 재귀함수를 이용한 풀이
def factorial(N):
    answer = 1
    if N==0 or N==1:
        return 1
    else:
        answer = N*factorial(N-1)
    return answer
N = int(input())
print(factorial(N))



N = int(input())
answer = 1
for i in range(1, N+1):
    answer *= i

print(answer)
