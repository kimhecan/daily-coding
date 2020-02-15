import unittest

def solution(s, n):
  
  lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
  arr = list(s)

  for i in range(0, len(arr)):
    if arr[i] in lower:
      num1 = lower.index(arr[i]) + n
      if num1 >= 26: num1 -= 26
      arr[i] = lower[num1]
    
    if arr[i] in upper:
      num2 = upper.index(arr[i]) + n
      if num2 >= 26: num2 -= 26
      arr[i] = upper[num2] 

  return "".join(arr)


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution('a',1),'b')
  
  def test_solution2(self):
    self.assertEqual(solution('z',1),'a')

  def test_solution3(self):
    self.assertEqual(solution('a B z',4),'e F d')


if __name__ == "__main__":
    unittest.main()