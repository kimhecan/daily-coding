### 1. 이해

탐색을 통해 단지의 갯수와 집의 갯수를 구하는 문제다.

https://www.acmicpc.net/problem/2667

### 2. 계획

이전에 미로찾기 문제에서 현재위치에서 위,아래,왼,오를 탐색해서 조건에 맞는다면 액션을 취해주는 방식을 사용하면 된다.

BFS로 풀듯. n * n을 전체를 탐색하는데 내용이 1이여야하고 방문하지 않았던 곳일 때 그 노드를 기점으로 상,하,좌,우를 탐색해 인덱스를 넘어가지 않고 1이라면 count를 증가시키고 방문리스트에 넣고 그 노드를 큐에 넣어 반복한다.


### 3. 실행


### 4. 반성

n*m 행렬이 나왔을 때 유용하게 사용할 수 있는 BFS 방법인것 같다. BFS로 탐색하든 DFS로 탐색하든 결과만 나오면..




### 4. 순서

문제 이해 - 문제계획 - 문제 풀기 - 실행 - 반성


from https://www.notion.so/4c76a62be47c424186e178e1e2c081d4
