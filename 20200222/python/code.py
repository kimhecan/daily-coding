import unittest

def solution(departList, budget):
  departList.sort()
  while sum(departList) > budget:
    departList.pop()
  
  return len(departList)


class MyTest(unittest.TestCase):
  def test_soution1(self):
    self.assertEqual(solution([1],3), 1)
    



if __name__ == "__main__":
    unittest.main()