from collections import deque


def solution():
  case = int(input())
  countList = []

  for _ in range(case):
    M, N, K = map(int, input().split(" "))
    matrix = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    q = deque()
    
    count = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for _ in range(K):
      x, y = map(int, input().split(" "))
      matrix[y][x] = 1

    for i in range(N):
      for j in range(M):
        if matrix[i][j] == 1 and visited[i][j] == 0:
          q.append((i,j))
          while q:
            x, y = q.popleft()

            for k in range(4):
              nx = x + dx[k]
              ny = y + dy[k]
              if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                  q.append((nx, ny))
                  visited[nx][ny] = 1
          count += 1
    countList.append(count)
  for i in range(len(countList)):
    print(countList[i])

solution()