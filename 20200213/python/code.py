import unittest

def solution(n):
    answer = 0
    for i in range(1, n//2 + 1):
      if n % i == 0: answer += i
    return answer


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEquals(solution(12), 28)
  
  def test_solution(self):
    self.assertEquals(solution(5), 6)



  
if __name__ == "__main__":
    unittest.main()