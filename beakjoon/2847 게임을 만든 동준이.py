# https://www.acmicpc.net/problem/2847

N = int(input())
score = []
decrease_amount = 0
for i in range(N):
    score.append(int(input()))
    
score.reverse()

for i in range(0, N-1):
    if score[i] > score[i+1]:
        pass
    else:
        decrease_amount += (score[i+1] - score[i] + 1)
        score[i+1] = score[i]-1
        
print(decrease_amount)
