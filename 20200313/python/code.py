import unittest

# def solution(N, stages):
#   arr = [(i, stages.count(i) / (len(list(filter(lambda x: x >= i, stages))) if len(list(filter(lambda x: x >= i, stages))) != 0 else 1) ) for i in range(1, N+1)]
#   arr.sort(key= lambda x: x[1], reverse=True)
#   print(list(map(lambda x: x[0], arr)))
  
def solution(N, stages):
  result = {}
  denominator = len(stages)
  for stage in range(1, N+1):
    if denominator != 0:
      count = stages.count(stage)
      result[stage] = count / denominator
      denominator -= count
    else:
      result[stage] = 0
  return sorted(result, key=lambda x: result[x], reverse=True)


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(5, [4,4,4,4,4])
