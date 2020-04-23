def solution():
  n = int(input())
  arr = [int(input()) for i in range(n)]
  arr.sort(reverse=True)
  sums = []
  for i, v in enumerate(arr):
    sums.append(v * (i+1))
  
  return max(sums)


print(solution())