
  
### 1회
```python
def solution(a, b):
    answer = 0
    if a <= b:
        answer = sum(range(a, b+1))
    else:
        answer = sum(range(b, a+1))
    return answer
```

### 2회
```python
def solution(a, b):
    if a>b:
        a, b = b, a
        return sum(range(a, b+1))
    else:
        return sum(range(a, b+1))
```

### 3회
```python
def solution(a, b):
    if a>b:
        a, b = b, a
        
    return sum(range(a, b+1))

```


### 다른 사람의 풀이

```python
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
print(adder(a, b))
```
