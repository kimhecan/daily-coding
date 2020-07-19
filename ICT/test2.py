def commonSubstring(a, b):
    for i in range(len(b)):
        for j in a[i]:
            if j in b[i]:
                print('YES')
                break
            if j == a[i][-1]:
                print('NO')
                break
