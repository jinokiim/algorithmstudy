# https://programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    answer = -1
    need = 0
    
    for n in range(1, count+1):
        need += n*price
        
    answer = need-money
    return answer if answer>=0 else 0
