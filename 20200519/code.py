from collections import deque

M, N, K = map(int, input().split(" "))

matrix = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

arr = []
for _ in range(K):
  arr.append(list(map(int, input().split(" "))))


for i in range(K):
  while arr[i][1] < arr[i][3]:
    tempX = arr[i][0]
    while tempX < arr[i][2]:
      matrix[arr[i][1]][tempX] = 1
      tempX += 1
    arr[i][1] += 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]

widthArr = []


for i in range(M):
  for j in range(N):
    if matrix[i][j] == 0 and visited[i][j] == False:
      count = 1
      visited[i][j] = True
      q = deque()
      q.append((i,j))
      while q:
        x, y = q.popleft()
        for v in range(4):
          nx = x + dx[v]
          ny = y + dy[v]
          if 0<= nx < M and 0<= ny < N:
            if matrix[nx][ny] == 0 and visited[nx][ny] == False:
              count += 1
              q.append((nx,ny))
              visited[nx][ny] = True
              matrix[nx][ny] = 2
      widthArr.append(count)
    
widthArr.sort()
print(len(widthArr))
print(" ".join(map(str,widthArr)))




