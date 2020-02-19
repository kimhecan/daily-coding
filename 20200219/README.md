### 1. 이해

최대공약수와 최소공배수를 구하는 문제다.

### 2. 계획

분명 관련된 공식이 있을 것이다. 찾아보자

### 3. 실행


### 4. 반성

최대공약수와 최소공배수를 구하는 공식중 유클리드 호제법이 있다는 것을 알게 되었다. 그러나 중요한 건 예전에 보고 풀어봤다는 것이다.. 1년전인가.. 역시 복습을 안하면 다 까먹는다. 금욜날에 첨부터 뭘 풀었는지 복습할 예정이다.

https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95


유클리드 호제법은 a > b에서 a % b 를 r 이라고 하면 a와  b의 최대공약수는 b와 r의 최대공약수와 같다.
이 성질을 이용한다. 

그래서 만든 코드가
```javascript
function solution(n, m) {
  let mul = n * m;
  while ( m !== 0) {
    r = n % m;
    n = m;
    m = r;
  }
  return [n, mul / n]
}
```
이거다 그런데 다른 사람은 재귀함수를 통해 풀었다. 그래서 파이썬언어로 배꼈다.

```python
def GreatestCommonDivisor(n, m): return GreatestCommonDivisor(m, n % m) if m != 0 else abs(n)

def LowestCommonMultiple(n, m): return n * m / GreatestCommonDivisor(n, m)

def solution(n, m):
  return [GreatestCommonDivisor(n, m), LowestCommonMultiple(n, m)]

```

오늘의 교훈: 복습하자.
### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
