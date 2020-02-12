import unittest
import math

def solution(n):
  arr = [True] * (n+1)
  arr[0] = arr[1] = False


  for i in range(2, int(math.sqrt(n))+1):
    mult = 2
    for j in range(i * mult, n+1, i):
      arr[j] = False
      mult += 1
  
  return len([i for i in range(2, n+1) if arr[i] == True])

  

class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(10), 4)
  
  def test_solution2(self):
    self.assertEqual(solution(5), 3)

if __name__ == "__main__":
    unittest.main()