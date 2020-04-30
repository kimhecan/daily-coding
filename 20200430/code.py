def solution():
  n, m, k = map(int, input().split(" "))
  team = 0
  while n >= 2 and m >= 1:
    n -= 2
    m -= 1
    team += 1
  

  #비율이 2:1로 딱 맞을 경우
  if n == 0 and m == 0:
    quotient = k // 3
    remainer =  k % 3
    team -= quotient
    if remainer > 0:
      team -=1
  #비율이 딱 맞지 않을 경우(n또는m이 남아있는경우)
  else:
    k -= (n+m)
    if k <= 0:
      return team
    else:
      quotient = k // 3
      remainer =  k % 3
      team -= quotient
      if remainer > 0:
        team -=1
  
  return team


print(solution())