import unittest


def solution(n):
  return n % sum(list(map(int, list(str(n))))) == 0



class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(12), True)
  
  def test_solution2(self):
    self.assertEqual(solution(10), True)

  def test_solution3(self):
    self.assertEqual(solution(11), False)

  
if __name__ == "__main__":
    unittest.main()