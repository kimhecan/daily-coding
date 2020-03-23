### 1. 이해

소수의 갯수를 구하는 문제다.


https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

### 2. 계획



### 3. 실행



### 4. 반성


우선 에라토스테네스의 체라는 것을 알고는 있었지만 완전히 이해하지 못했고
루트 n까지만 검사해야하는 이유도 정확히 몰랐었다. 

결국 못풀고 답지를 봄..

차피 길이를 구하는 문제라서 파이썬에서 집합을 이용해 2의배수 3의배수..빼면
더 간단한 코드가 나온다..


```python
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

```
b

### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
