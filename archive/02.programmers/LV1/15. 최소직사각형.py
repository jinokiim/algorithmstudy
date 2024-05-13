# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    width = 0
    height = 0
    
    for i in range(len(sizes)):
        # 인덱스에서 가로가 더 길다면
        if sizes[i][0] > sizes[i][1]:
            # 가로세로를 바꾸어서 width, height 최신화
            width = max(width, sizes[i][1])
            height = max(height, sizes[i][0])
        else: # 아닐경우엔 그대로 width, height 입력
            width = max(width, sizes[i][0])
            height = max(height, sizes[i][1])
    # 넓이 return
    return width*height
