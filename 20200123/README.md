### 1. 이해

두수 사이에 합을 구하는 문제다

### 2. 계획

경우가 3가지 이므로 경우에 따라 처리한다.

### 3. 실행



### 4. 반성


#### python

파이썬에 sum은 리스트를 인자로 받기 때문에 range를 이용하면 더 쉽게 풀 수 있었다.

```python

def adder(a, b):

    if a > b: a, b = b, a

    return sum(range(a,b+1))

```