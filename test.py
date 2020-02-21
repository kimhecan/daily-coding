def solution(x, n):
  if x == 0: return [0] * n
  return [i for i in range(x, x*n+1, x)] if x > 0 else [i for i in range(x, x*n-1, x)]
  



print(solution(2, 5))
print(solution(-4,2))
print(solution(2, 5))
print(solution(-4,1))
print(solution(0, 5))