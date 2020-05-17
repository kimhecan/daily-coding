from sys import stdin
from collections import deque

def bfs():
  N, M = map(int, stdin.readline().split(" "))
  obj = {}
  for i in range(N):
    obj[i+1] = []

  for _ in range(M):
    u, v = map(int, stdin.readline().split(" "))
    obj[u].append(v)
    obj[v].append(u)
  
  count = 0
  visited = [0] * (N + 1)
  
  for i in range(1, N+1):
    if visited[i] == 0:
      count += 1
      q = deque([i])    
      while q:
        x = q.popleft()
        for j in obj[x]:
          if visited[j] == 0:
            q.append(j)
            visited[j] = 1
  
  print(count)


# def dfs(v):
#   visited[v] = 1
#   for i in obj[v]:
#     if visited[i] == 0:
#       dfs(i)

# N, M = map(int, stdin.readline().split(" "))
# obj = {}
# for i in range(N):
#   obj[i+1] = []

# for _ in range(M):
#   u, v = map(int, stdin.readline().split(" "))
#   obj[u].append(v)
#   obj[v].append(u)

# count = 0
# visited = [0] * (N + 1)


# for i in range(1, N+1):
#   if visited[i] == 0:
#     count += 1
#     dfs(i)


# print(count)      
