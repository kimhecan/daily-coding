from sys import stdin
from collections import deque
from itertools import combinations

N, M = map(int, stdin.readline().split(" "))

matrix = [list(stdin.readline().rstrip().replace(" ", "")) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

arrZero = []

for i in range(N):
  for j in range(M):
    if matrix[i][j] == "0":
      arrZero.append((i, j))

com = list(combinations(arrZero,3))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

resultArr = []
for v in com:
  for c in v:
    matrix[c[0]][c[1]] = "4"

  for i in range(N):
    for j in range(M):
      if matrix[i][j] == "2" and visited[i][j] == False:
        visited[i][j] = True
        q = deque()
        q.append((i,j))
        while q:
          x, y = q.popleft()
          for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny<M:
              if matrix[nx][ny] == "0" and visited[nx][ny] == False:
                q.append((nx,ny))
                matrix[nx][ny] = "3"
                visited[nx][ny] = True
  count = 0
  for i in range(N):
    for j in range(M):
      if matrix[i][j] == "0":
        count += 1
  resultArr.append(count)

  for i in range(N):
    for j in range(M):
      if matrix[i][j] == "3" or matrix[i][j] == "4":
        matrix[i][j] = "0"
  visited = [[False]*M for _ in range(N)]

  

print(max(resultArr))





  
  


