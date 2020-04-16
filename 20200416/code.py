money = int(input())
changeMoney = 1000 - money
arr = [500, 100, 50, 10, 5, 1]
count = 0

for i in arr:

  if changeMoney // i > 0:
    count += changeMoney // i
    changeMoney -=  i * (changeMoney // i)

print(count)

#https://www.acmicpc.net/problem/5585