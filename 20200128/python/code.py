import unittest

def solution(arr):
  answer = [arr[0]]
  for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
      continue
    answer.append(arr[i])
  return answer




class MyTests(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution([1,1,3,3,0,1,1]),[1,3,0,1])
  def test_solution2(self):
    self.assertEqual(solution([4,4,4,3,3]),[4,3])


if __name__ == "__main__":
    unittest.main()