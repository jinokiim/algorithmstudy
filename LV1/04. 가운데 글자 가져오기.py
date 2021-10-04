
## **풀이**
### 1회차
```python
def solution(s):
    answer = ''
    l = len(s)
    if l % 2 == 1:
        answer = s[(l//2)]
    else:
        answer = s[l//2-1:l//2+1]
    return answer
```
### 2회차
```python
def solution(s):
    a = len(s)
    if a%2==0:
        return s[a//2-1] + s[a//2]
    else: return s[a//2]
```

## 다른 사람의 풀이

```python
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
```
