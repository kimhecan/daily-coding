def solution():
    n, k = map(int,input().split(" "))
    arr = [int(input()) for i in range(n)]
    count = 0
    for i in range(1,len(arr)+1):
        if k // arr[-i] > 0:
            count += k // arr[-i]
            k = k % arr[-i]
    return count

print(solution())