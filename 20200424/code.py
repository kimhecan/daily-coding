def solution(n):
  if n % 10 != 0 or n % 3 != 0:
    return -1
  else {
    s = sotred(list(map(int,list(str(n //10)))), reversed=True)
  }