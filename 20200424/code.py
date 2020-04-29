def solution():
  n = int(input()) 
  arr = list(str(n))
  arr.sort(reverse=True)

  #10의 배수 아니면 -1
  if '0' not in arr: return -1
  #3의 배수 아니면 -1
  if n % 3 != 0: return -1

  answer = int(''.join(arr))

  return answer

print(solution())