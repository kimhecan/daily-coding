def solution(people, limit):
  people.sort()
  shipCount = 0
  light = 0
  heavy = len(people) -1

  while light <= heavy:
    shipCount += 1
    if people[light] + people[heavy] <= limit:
      light+= 1
    heavy -= 1
  return shipCount



  




# 전형적인 예
print(solution([70,50,80,50],100)) #3
print(solution([70, 80, 50],100)) # 3
print(solution([70, 80],100)) # 2
print(solution([40,50,60,70,80,90],100)) #5
# 다합쳐도 한계치미만
print(solution([40,50],100)) #1
print(solution([10,20,30],100)) #2
print(solution([10,10,10,20,30],100),"3개인가요") #3
# 다합친게 한계치
print(solution([50,50],100)) #1
# 한개만있을 때
print(solution([50],100)) #1
print(solution([100,10],100)) #2