import collections
def solution():
    inputOne = []
    inputTwo = []
    for i in range(0,8):
        a, b = input().split()
        inputOne.append(a)
        inputTwo.append(b)

    counterOne = collections.Counter(inputOne)
    counterTwo = collections.Counter(inputTwo)
    print(counterOne)
    print(counterTwo)

    for i, j in zip(counterOne.values(),counterTwo.values()):
        if i > 1 or j > 1:
            print("YES")
            return 0
    print("NO")
    

solution()
    
    
    
