from sys import stdin
from collections import deque

M,N = map(int, stdin.readline().split(" "))

matrix = [stdin.readline().rstrip().split(" ") for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

count = 1

basket = deque()


for i in range(N):
  for j in range(M):
    if matrix[i][j] == "1":
      basket.append((i,j))


while basket:
  x, y = basket.popleft()
  if matrix[x][y] == str(count):
    count += 1
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and matrix[nx][ny] == "0":
      matrix[nx][ny] = str(count)
      basket.append((nx, ny))
      visited[nx][ny] = 1


for i in range(N):
  if "0" in matrix[i]:
    print("-1")
    break
  if i == N-1:
    print(count-2)
  
    

  
