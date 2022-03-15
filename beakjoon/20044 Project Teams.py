# https://www.acmicpc.net/problem/20044

s = int(input())
w_list = list(map(int, input().split()))

# 정렬
w_list.sort()
# 각 팀의 w를 넣을 list
w = []

for i in range(s):
    # 바깥쪽부터 하나씩 안쪽으로 합계를 w에 추가
    w.append(w_list[i] + w_list[-i-1])
    
# 가장 합이 작은w 출력
print(min(w))
