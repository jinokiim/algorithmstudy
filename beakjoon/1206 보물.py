# https://www.acmicpc.net/submit/1026

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

A.sort()
B.sort()
for i in range(N):
    S += A[i] * B[-1-i]
    
print(S)
