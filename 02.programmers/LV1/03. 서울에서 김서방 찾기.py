
## **풀이**
### 1회차
```python
def solution(seoul):
    answer = ''
    kim = seoul.index('Kim')
    answer = '김서방은 ' + str(kim) + '에 있다'
    return answer
```
### 2회차
```python
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return '김서방은 {}에 있다'.format(i)
```

## 다른 사람의 풀이

```python
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
```
