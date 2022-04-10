# 문제 출처
# https://yummy-silence-a74.notion.site/dd0374867eeb4196a8b9b9b42929f8e0

def ant_sequence(n):
    # 초기정답 1
    answer = '1'
    
    # n=1일때 0단계를 실행하기 위해 n-1로 수행
    for _ in range(n-1):
        count = 1   # 몇번 연속 있는지
        compared_num = answer[0]   # 값을 비교할 기준
        new_string = ''  # 이어붙이기 위한 문자열
    
        # 0번인덱스에서 시작하고, 1번째 인덱스부터 비교
        for pin in range(1, len(answer)):
        
            # 기준값과 다음 인덱스와 같으면
            if answer[pin] == compared_num:
                # 갯수 추가
                count += 1

            else: # 다르면
                # 기준숫자와 몇개인지 이어붙이기 / 예) 기준이었던 2가 3번나온다. => 23
                new_string += str(compared_num) + str(count)
                # 기준되는 숫자 변경
                compared_num = answer[pin]
                # count 1로 초기화
                count = 1
        # 제일처음 '1' 에 추가된 문자열 추가  (마지막에 같은경우로 반복문 종료로 인해 str(compared_num) + str(count))        
        answer = new_string + str(compared_num) + str(count)

    # 정답 반환    
    return answer
