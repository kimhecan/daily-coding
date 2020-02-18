import unittest

def solution(n):
  count = 0;
  while n != 1:
    if n % 2 == 0: n = n/2;
    else: n = n*3 + 1;
    count += 1
    if count == 500: return -1
  
  return count


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(6), 8)
  
  def test_solution2(self):
    self.assertEqual(solution(16), 4)

  def test_solution3(self):
    self.assertEqual(solution(626331), -1)

if __name__ == '__main__':
    unittest.main()
    