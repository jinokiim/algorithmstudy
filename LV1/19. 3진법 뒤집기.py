# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    first_step = []
    second_step = []

    while n > 0:
        n, rest = divmod(n, 3)
        first_step.insert(0, str(rest))

    first_step = int(''.join(first_step))
    second_step = int(str(first_step)[::-1])
    answer = int(str(second_step), 3)
    return answer
