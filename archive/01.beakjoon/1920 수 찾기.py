# 첫번째 풀이
import sys

N = int(input())
NA = list(map(int, sys.stdin.readline().split()))

M = int(input())
MA = list(map(int, sys.stdin.readline().split()))

for i in MA:
    if i in NA:
        print('1')
    else:
        print('0')

        
# 두번째 풀이
import sys

def bisearch(arr, val, start, end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==val:
            return True
        if arr[mid] > val:
            end = mid-1
        elif arr[mid] < val:
            start = mid+1
        else:
            return False

N = int(input())
NA = list(map(int, sys.stdin.readline().split()))
NA.sort()

M = int(input())
MA = list(map(int, sys.stdin.readline().split()))

for i in MA:
    if bisearch(NA, i, 0, N-1):
        print(1)
    else:
        print(0)


