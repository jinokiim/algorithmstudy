# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = b-1
    
    for i in range(a-1):
        day += month[i]

    answer = day_list[day%7]

    
    return answer

