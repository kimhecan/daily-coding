def insertion(x, ss):
  if ss != []:
    if x <= ss[0]:
      return [x] + ss
    else:
      return [ss[0]] + insertion(x, ss[1:]) 
  else:
    return [x]


print(insertion(4,[1,2,3,5,6]))
print(insertion(7,[1,2,3,5,6]))
