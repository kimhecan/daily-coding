n = int(input())
arr = [int(input()) for _ in range(n)]

dynamic = [0,1,2,4,0,0,0,0,0,0,0]

for i in range(4, 11):
  dynamic[i] += dynamic[i-1] + dynamic[i-2] + dynamic[i-3]


for i in arr:
  print(dynamic[i])


