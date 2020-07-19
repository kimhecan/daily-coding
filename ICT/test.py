def countGroups(related):
    gCount = len(related)
    checkArr = []
    checkArr2 = []
    for i in range(len(related)):
        for j in range(len(related)):
            if i >= j:
                continue
            if related[i][j] == '1':
                # 처음 1을 만났을 때는 무조건 추가한다.
                if len(checkArr) == 0:
                    checkArr.append(set([i, j]))
                    continue
                # 두번째로 만났을 때부터 연결될 수 있는게 있는지 확인한다.
                leen = len(checkArr)
                for k in range(leen):
                    if i in checkArr[k]:
                        checkArr[k].add(j)
                        break
                    if j in checkArr[k]:
                        checkArr[k].add(i)
                        break
                    if k == (leen - 1):
                        checkArr.append(set([i, j]))

    # test
    a = []
    for i in checkArr:
        for j in i:
            a.append(j)
    last = len(a) - len(set(a))

    if len(checkArr) == 0:
        return len(related)

    count = 0
    for i in range(len(related)):
        for j in range(len(checkArr)):
            if i in checkArr[j]:
                break
            if j == (len(checkArr) - 1):
                count += 1
                break

    return len(checkArr) + count - last


related_count = int(input().strip())

related = []

for _ in range(related_count):
    related_item = input()
    related.append(related_item)

print(countGroups(related))
# print(countGroups(['1100', '1110', '0110', '0001']))
# print(countGroups(['11111', '11111', '11111', '11111', '11111']))
# print(countGroups(['10000', '01000', '00100', '00010', '00001']))
