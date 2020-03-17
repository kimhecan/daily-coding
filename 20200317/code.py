import re

def solution(dartResult):
    arrAll = re.compile('\d+\w[\*\#]?').findall(dartResult)
    arrDigit = list(map(int, re.compile('\d+').findall(dartResult)))
    for i, v in enumerate(arrAll):
      if re.compile('\w').findall(v)[-1] == 'D':
        arrDigit[i] = arrDigit[i] ** 2
      elif re.compile('\w').findall(v)[-1] == 'T':
        arrDigit[i] = arrDigit[i] ** 3
      else: 
        arrDigit[i]
      
      if len(re.compile(r'\*').findall(v)) == 1:
        if i == 0:
          arrDigit[i] *= 2
        else:
          arrDigit[i-1] *= 2
          arrDigit[i] *= 2
      if len(re.compile(r'\#').findall(v)) == 1:
        arrDigit[i] = -arrDigit[i]
    return sum(arrDigit)
 



print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1T2D3D#"))
print(solution("10D1S1T*"))