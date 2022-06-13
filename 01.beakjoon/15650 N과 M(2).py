# https://www.acmicpc.net/problem/15650

N, M = map(int, input().split())

answer = []

def solution(depth, N):
    # 반환할 길이가 되면
    if len(answer) == M:
        # 출력
        print(' '.join(map(str, answer)))
        return # 조건을 만족할때 반복문을 빠져나온다.
                # 1부터 4까지 반복
    for i in range(depth, N+1):
        # answer에 i 가 없으면
        if i not in answer:
            # 반환할 배열에 i 추가
            answer.append(i)
            # 함수호출
            solution(i+1, N)
            # 계속진행하도록 제일오른쪽 요소 제거
            answer.pop()
            
solution(1, N)
