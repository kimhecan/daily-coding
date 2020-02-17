import unittest
import math



def solution(n):
  return math.pow(math.sqrt(n) + 1, 2) if math.sqrt(n).is_integer() else -1 


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(121), 144)
  
  def test_solution2(self):
    self.assertEqual(solution(3), -1)
  


if __name__ == '__main__':
    unittest.main()
    