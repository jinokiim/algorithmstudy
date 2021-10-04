
## **풀이**

# 1회차
def solution(n):
    answer = ''
    if n % 2 == 0 :
        answer = ('수박' * int(n / 2))
    else :
        answer = ('수박' * int(n / 2) + '수') 
    
    return answer

# 2회차
```python
def solution(n):
    answer = ''
    wm = '수박'
    if n%2==0:
        answer = wm * (n//2)
    else:
        answer = wm*(n//2)+'수'
    return answer


