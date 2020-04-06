# def solution():
#   expression = list(input())
#   if expression[0] == "0": expression.remove("0")
#   expression.insert(0, "(")
  
#   for i, item in enumerate(expression):
#     if item == "-" or item == "+": 
#       if expression[i+1] == "0" and expression[i+1] != expression[len(expression) -1]:
#         expression[i+1] = ""
#     if item == "-": expression[i] =  ")"+ expression[i] + "("
#   expression.append(")")
#   return (eval("".join(expression)))

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

#다른 방법을 생각해 보자.. 한 방법만 고집하지 말고,,