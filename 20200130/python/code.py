import unittest
import re

def solution(s):
    regEx = re.compile('^\d{4,4}$|^\d{6,6}$')
    answer = regEx.match(s)
    return False if answer == None else True  


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution("a123"), False)
  
  def test_solution2(self):
    self.assertEqual(solution("1234"), True)


if __name__ == "__main__":
    unittest.main()