from collections import deque

def solution():
  N = int(input())
  arr = [list(map(int, input().split(" "))) for _ in range(N)]
  answer = [['0'] * N for _ in range(N)]
  obj = {}
  for i in range(0, N):
    obj[i] = []
  
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 1:
        obj[i].append(j)

  for i in range(N):
    visited = [False for _ in range(N)]
    arr = []
    for j in range(N):
      q = deque([i])
      while q:
        x = q.popleft()
        for k in obj[x]:
          if visited[k] == False:
            visited[k] = True
            q.append(k)
            arr.append(k)
    for v in arr:
      answer[i][v] = '1'
  
  for i in answer:
    print(' '.join(i))



solution()
  