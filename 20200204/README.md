### 1. 이해

https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3


배열과 이중배열이 주어졌다. 배열을 다룰 수 있나 물어보는 문제다.

### 2. 계획

js 에서는 map, slice, sort 함수를 이용해서 해결한다.

반복문으로 이중배열길이 만큼 반목하고 그 안에 배열에 첫번쨰부터 세번째
인덱스까지 활용

### 3. 실행


### 4. 반성

lambda와 map함수를 활용하지 못했다.
```python
list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```

### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
