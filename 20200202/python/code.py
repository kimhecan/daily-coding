import unittest
import re

def solution(s):
  regxP = re.compile('p').findall(s.lower())
  regxY = re.compile('y').findall(s.lower())

  return True if len(regxP) == len(regxY) else False



class myTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution("pPoooyY"), True)
  
  def test_solution2(self):
    self.assertEqual(solution("Pyy"), False)


if __name__ == "__main__":
    unittest.main()