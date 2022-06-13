def solution(s):
    # 알파벳 내림차순으로 정렬(리스트로 반환), 대문자의 아스키코드값이 더 작아 문제조건을 만족한다.
    answer = sorted(s, reverse=True)
    # 리스트 원소들을 공백없이 붙여서 출력
    answer = ''.join(answer)
    return answer
