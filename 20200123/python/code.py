import unittest


def solution(a, b):
  answer = 0
  if a < b:
    while a <= b:
      answer += a
      a += 1
  elif a > b:
    while a >= b:
      answer += b
      b += 1
  else:
    answer = a
  
  return answer

  # def adder(a, b):
  #   if a > b: a, b = b, a

  #   return sum(range(a,b+1))



class MyTests(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(3, 5), 12)
  def test_solution2(self):
    self.assertEqual(solution(5, 3), 12)
  def test_solution3(self):
    self.assertEqual(solution(3, 3), 3)


if __name__ == "__main__":
    unittest.main()