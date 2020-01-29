import unittest

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution([1,2,3,4]),2.5)
  def test_solution2(self):
    self.assertEqual(solution([5,5]), 5)


if __name__ == "__main__":
    unittest.main()