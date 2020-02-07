import unittest


def solution(answers):
    answer = []
    scores = [0,0,0]

    v1 = [1, 2, 3, 4, 5]
    v2 = [2, 1, 2, 3, 2, 4, 2, 5]
    v3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(0, len(answers)):
      if answers[i] == v1[i % len(v1)]:
        scores[0] += 1
      
      if answers[i] == v2[i % len(v2)]:
        scores[1] += 1
      
      if answers[i] == v3[i % len(v3)]:
        scores[2] += 1
   
    maxScore = max(scores)

    if maxScore == scores[0]:
      answer.append(1)

    if maxScore == scores[1]:
      answer.append(2)

    if maxScore == scores[2]:
      answer.append(3)

    return answer



class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution([1,2,3,4,5]), [1])

  def test_solution2(self):
    self.assertEqual(solution([1,3,2,4,2]), [1,2,3])


if __name__ == "__main__":
    unittest.main()