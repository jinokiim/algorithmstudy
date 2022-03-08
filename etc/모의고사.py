# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    count_one = 0
    count_two = 0
    count_three = 0
    gaveup_one = [1, 2, 3, 4, 5]  # 5
    gaveup_two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    gaveup_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    
    for i in range(len(answers)):
        if answers[i] == gaveup_one[i%5]:
            count_one+=1
        if answers[i] == gaveup_two[i%8]:
            count_two+=1
        if answers[i] == gaveup_three[i%10]:
            count_three+=1
            
    print(count_one, count_two, count_three)
    count = max(count_one, count_two, count_three)
    if count_one == count:
        answer.append(1)
    if count_two == count:
        answer.append(2)
    if count_three == count:
        answer.append(3)
            

    return answer
