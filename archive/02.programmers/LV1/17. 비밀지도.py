# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    addarr = []
    for i in range(n):
        element = str(int(format(arr1[i], 'b')) + int(format(arr2[i], 'b')))
        element = str(element).zfill(n)
        map_line = ''

        for j in element:
            if j == '0':
                map_line += ' '
            else:
                map_line += '#'
            
        answer.append(map_line)

    return answer
