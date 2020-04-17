import sys
read = sys.stdin.readline

n = int(read())
arr = []
for i in range(n):
  a, b = map(int, read().split())
  arr.append((b, a))

arr.sort()

print(arr)

y_min, cnt = 0, 0
for b, a in arr:
  if a >= y_min:
    y_min = b
    cnt += 1

print(cnt)












# conferNum = int(input())
# conferList = []
# for i in range(0, conferNum):
#   conferList.append(list(map(int, input().split())))
# conferList.sort(key=lambda x: x[10])
# conferList.sort(key=lambda x: x[1])

# end = answer = 0

# for m in conferList:
#   if end <= m[0]:
#     end = m[1]
#     answer += 1

# print(answer)

#https://www.acmicpc.net/problem/1931