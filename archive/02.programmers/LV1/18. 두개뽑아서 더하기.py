# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                pass
            else:
                answer.append(numbers[i]+numbers[j])
    
    sorted(list(set(answer)))
    
    return answer
