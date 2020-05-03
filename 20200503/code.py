from collections import deque

def solution():
  point, line, startNum = map(int, input().split(" "))
  graph = {}
  for i in range(point):
    graph[i+1] = []

  
  for i in range(line):
    start, end = map(int, input().split(" "))
    graph[start].append(end)
    graph[end].append(start)
  
  for i in range(point):
    graph[i+1].sort()

  dfs([], graph, startNum)
  print('')
  bfs([], graph, startNum)
  


def dfs(visited, graph, node):
  if node not in visited:
    print(node, end=" ")
    visited.append(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)


      

def bfs(visited, graph, node):
  queue = deque([node])
  visited.append(node)

  while queue:
    s = queue.popleft()
    print(s, end=" ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)





solution()