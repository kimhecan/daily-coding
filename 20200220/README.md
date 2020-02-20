### 1. 이해

각자리수를 더한 값이 원래값을 나눴을때 나눠떨어지면 true 아니면 false

### 2. 계획

reduce함수 사용

### 3. 실행


### 4. 반성

javascript 경우에 reduce함수의 사용법을 까먹은거 같아 복습함.. 

또한 '1'이런식으로 있을 때 Number('1') 이렇게 타입변환해도 되지만 +'1'을 해도 타입변환이 됨


```python
# 숫자를 string으로 바꾸고 리스트로 바꾸고 map으로 각 값을 int형으로 바꾸고 리스트로 반환하는 거랑
sum(list(map(int, list(str(a)))))


# 숫자를 string으로 바꾸고 반복문으로 나온값을 int형으로 리스트값으로 담아주는거
sum([int(c) for c in str(n)])

# 결론.. 문자열은 반복문이 가능하다....
```
### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
