### 1. 이해

https://www.acmicpc.net/problem/10610


숫자가 주어질 때 그 숫자를 조합해서 30의 배수중 가장 큰거 리턴(30배수 안되면 -1 리턴)

### 2. 계획


0 이 들어가 있는지 확인하고 그 다음 각자리 숫자를 더해 3의 배수이면 3의배수이기때문에 정렬해서 리턴하면 될듯?


### 3. 실행


### 4. 반성

일단 파이썬에서 리스트안에 내가 찾고 있는 수가 없는지 확인할 땐
```python
if '0' not in arr:

```
이런 식으로 하면 된다는 것을 알게됐다. 진작에 풀었는데 input()받는걸 함수 인자로 넣어서 계속 틀렸다...
그덕에 코드가 좀 깔끔해지긴 했다.

그리고 리스트에서 문자가 담겨있어도 숫자형이면 비교가 된다.
그리고 js에서 includes는 문자열 배열 둘다 사용가능하다.

어떤게 포함되어있는지 아닌지 빠르게 확인할 때 유용할거같다.


### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
