import sys

def solution():
  n = int(input())
  arr = list(map(int, sys.stdin.readline().split()))
  arr.sort()
  time = 0
  for i in range(n):
    time += sum(arr[:i+1])

  return time

print(solution())


## 그리디문제였고 작은 순으로 정렬하고 각각 더해주면 된다