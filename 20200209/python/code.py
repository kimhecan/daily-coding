import unittest

def solution(arr, divisor):
    answer = sorted(filter(lambda x: x % divisor == 0, arr))

    return answer if len(answer) > 0 else [-1]

class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution([5, 9, 7, 10],5), [5, 10])
  
  def test_solution2(self):
    self.assertEqual(solution([2, 36, 1, 3],1), [1, 2, 3, 36])
  
  def test_solution3(self):
    self.assertEqual(solution([3,2,6],10), [-1])


if __name__ == "__main__":
    unittest.main()