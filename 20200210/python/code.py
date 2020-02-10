import unittest

def solution(s):
  answer = "".join(sorted(list(s))[::-1])
  return answer


class MyClass(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution('abc'), 'cba')
  
  def test_solution2(self):
    self.assertEqual(solution('Zbcdefg'), 'gfedcbZ')



if __name__ == "__main__":
    unittest.main()