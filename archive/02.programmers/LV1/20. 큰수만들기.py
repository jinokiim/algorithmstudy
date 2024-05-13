# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    # k가 0이면 그대로 return
    if k == 0:
        return number
    # int로 변환하면 시간초과여서 문자열 비교로 진행
    # 리스트 생성
    number = list(number)
    # 첫번째 숫자는 들어간채로 정답 list 생성
    answer = [number[0]]
    count = 0

    for i in range(1, len(number)):
        # 다음수 배열에 추가
        answer.append(number[i])
        # 반복문 실행
        while(len(answer) != 1 and answer[-1] > answer[-2] and count < k):
            # 추가된 요소가 이전보다 크면
            if answer[-1] > answer[-2]:
                # 제거하기 위해서 맨뒤로 보내고
                answer[-1], answer[-2] = answer[-2], answer[-1]
                # 제거
                answer.pop()
                count+=1

    return ''.join(answer[:len(number)-k])
