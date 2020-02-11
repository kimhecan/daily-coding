import unittest

def solution(arr1, arr2):
    answer = arr1
    for i, v in enumerate(arr1):
        for j, k in enumerate(arr2[i]):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer

class MyTest(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(solution([[1,2],[2,3]],[[3,4],[5,6]]), [[4,6],[7,9]])
    def test_solution2(self):
        self.assertEqual(solution([[1],[2]],[[3],[4]]), [[4],[6]])


if __name__ == "__main__":
    unittest.main()