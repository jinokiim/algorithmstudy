# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    s = s.lower()
    
    count_p = s.count('p')
    count_y = s.count('y')

    return True if count_p == count_y else False
