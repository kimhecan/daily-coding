### 1. 이해

https://www.acmicpc.net/problem/2217

여러개의 로프가 주어지고 각 로프가 들 수 있는 최대 무게가 주어진다.

이 로프들을 사용해서 최대로 들어올릴 수 있는 무게를 구하라

2개를 사용하면 무게도 절반이 된다.

무게를 n 으로 나눠도 그 나눈무게 보다 하나라도 로프가 들 수있는 무게가 작으면 실패다.

### 2. 계획

가장 무거운 것부터 최대무게를 구하고 그 다음 무거운거를 더하고 최대무게를 구하는 방식으로 다 구하고
그 리스트 중에 최대무게를 리턶나다.

### 3. 실행


### 4. 반성

선택 정렬이랑 비슷하게 탐색한다. 전체의 경우를 구하는 방법보다는 이전의 최댓값이 이후 최댓값보다 크다면

이전의 최댓값이 최댓값이라는 점을 활용해 탐색을 줄일 수 있다.

그리디 접근법이 활용되었다. 





### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
