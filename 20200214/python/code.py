import unittest

def solution(strings, n):
    return list(map(lambda x: x[1:], sorted(list(map(lambda x: x[n] + x, strings)))))
    
    

class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(['sun', 'bed', 'car'], 1), 	['car', 'bed', 'sun'])
  
  def test_solution2(self):
    self.assertEqual(solution(['abce', 'abcd', 'cdx'], 2),	['abcd', 'abce', 'cdx'])


if __name__ == '__main__':
    unittest.main()
    