def solution():
  expression = input().split("-")
  sum = 0

  for i in expression[0].split("+"):
    sum += int(i)
    
  for i in expression[1:]:
    for j in i.split("+"):
      sum -= int(j)
  return sum

print(solution())