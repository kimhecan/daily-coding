### 1. 이해

모든 약수를 더하는 문제다.

### 2. 계획

n이 나눠지면 된다.

### 3. 실행


### 4. 반성

검사할 때 1~n까지 검사할 필요없이 n//2까지만 검사해도 된다...

```python

return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

```

그리고 list comprehension을 사용하지 않았다는점...

list comprehension은 list를 쉽게 만들어주는 문법이다.

```python

evens = [x * 2 for x in range(11)]

non_squars = [x for x in range(101) if sqrt(x)**2 != x]

solutions = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]

```
### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
