# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in numbers:
        num_list.remove(i)

    return sum(num_list)
