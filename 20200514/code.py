from sys import stdin
from collections import deque
# def solution():  
#   N, K = map(int, stdin.readline().split(" "))
#   q = deque()
#   q.append([N])
#   count = 0
#   visited = set([N])
#   while True:
#     x = q.popleft()
#     print(x)
#     if K not in x:
#       arr = []
#       for i in range(len(x)):
#         if x[i]-1 not in visited:
#           arr.append(x[i]-1)
#         if x[i]+1 not in visited:
#           arr.append(x[i]+1)
#         if x[i]*2 not in visited:
#           arr.append(x[i]*2)
#       q.append(list(set(arr)))
#       visited.update(set(arr))
#     else:
#       break
#     count += 1
#   return count
      


# print(solution())



def bfs():
  q = deque()
  q.append(N)
  while q:
    v = q.popleft()
    if v == K:
      print(time[v])
      return
    for next_step in (v-1, v+1, v*2):
      if 0<= next_step < MAX and not time[next_step]:
        time[next_step] = time[v] + 1
        q.append(next_step)

MAX = 100001
N, K = map(int, stdin.readline().split(" "))
time = [0] * MAX
bfs()





















