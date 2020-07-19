import math
from collections import deque


def connectedSum(n, edges):
    obj = {}
    for i in range(n):
        obj[i+1] = []

    for v in edges:
        obj[int(v[0])].append(int(v[1]))
        obj[int(v[1])].append(int(v[0]))

    visited = [0] * (n + 1)

    storage = set()
    result = []

    for i in range(1, n+1):
        if visited[i] == 0:
            q = deque([i])
            while q:
                x = q.popleft()
                storage.add(x)
                for j in obj[x]:
                    if visited[j] == 0:
                        q.append(j)
                        visited[j] = 1
            result.append(storage)
            storage = set()
    arr = list(map(lambda x: len(x), result))

    return sum(list(map(lambda x: math.ceil(x**0.5), arr)))
