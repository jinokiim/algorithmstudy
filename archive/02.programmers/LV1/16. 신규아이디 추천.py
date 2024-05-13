# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):  
    answer = ''
    step1, step2, step3, step4, step5, step6, step7 = '', '', '', '', '', '', ''

    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    step1 = new_id.lower()

    
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for i in step1:
        if (ord(i) >96 and ord(i)<123) or (ord(i) >47 and ord(i)<58) or ord(i) == 45 or ord(i) == 46 or ord(i) == 95:
            step2 += i

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    step3 = step2
    while '..' in step3:
        step3 = step3.replace('..', '.')
    
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    step4 = step3
    if len(step4) > 0:
        if step4[0] == '.':
            step4 = step4[1:]
        elif step4[-1] == '.':
            step4 = step4[:-1]
    
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(step4) == 0:
        step5 = 'a'
    else: step5 = step4
        
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    step6 = step5
    if len(step6) >= 16:
        step6 = step6[:15]
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if step6[-1] == '.':
        step6 = step6[:-1]

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(step6) <= 2:
        step7 = step6 + step6[-1]*(3-len(step6))
    else: step7 = step6
    print('step7: ', step7)    
    answer = step7
    
    return answer

#
