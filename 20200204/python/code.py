import unittest


def solution(array, commands):
  arr = []
  for v in commands:
    arr.append(sorted(array[v[0] - 1: v[1]])[v[2]-1 : v[2]][0])
  return arr

class MyTests(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]),[5, 6, 3])

if __name__ == "__main__":
    unittest.main()
