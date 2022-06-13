# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d1 = sorted(d, reverse = False)
    count = 0
    
    for i in range(len(d1)):
        if d1[i] <= budget:
            budget -= d1[i]
            answer +=1
        
    return answer
