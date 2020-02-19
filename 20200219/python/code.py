import unittest

def GreatestCommonDivisor(n, m): return GreatestCommonDivisor(m, n % m) if m != 0 else abs(n)

def LowestCommonMultiple(n, m): return n * m / GreatestCommonDivisor(n, m)

def solution(n, m):
  return [GreatestCommonDivisor(n, m), LowestCommonMultiple(n, m)]


class MyTest(unittest.TestCase):
  def test_solution(self):
    self.assertEqual(solution(3, 12), [3, 12])
  
  def test_solution2(self):
    self.assertEqual(solution(2, 5), [1, 10])



if __name__ == "__main__":
    unittest.main()