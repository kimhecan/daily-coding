n = int(input())
arr = [list(map(int,input().split(" "))) for _ in range(n)]

for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      arr[i][j] += arr[i-1][0]
      continue
    if j == i:
      arr[i][j] += arr[i-1][i-1]
      continue
    arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])

print(max(arr[-1]))
    
    

