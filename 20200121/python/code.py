import unittest
import collections

def solution(participant, completion):
  answer = collections.Counter(participant) - collections.Counter(completion)
  return list(answer.key())[0]
  # obj = {}
  # for i in participant:
  #   if i in obj:
  #     obj[i] += 1
  #   else:
  #     obj[i] = 1
      
  # for i in completion:
  #   obj[i] -= 1 
  
  # for i in participant:
  #   if obj[i] == 1:
  #     return i

class MyTests(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(["leo", "kiki", "eden"],["eden", "kiki"]), "leo")
  def test_solution2(self):
    self.assertEqual(solution(["marina", "josipa", "nikola", "vinko", "filipa"]	,["josipa", "filipa", "marina", "nikola"]), "vinko")
  def test_solution3(self):
    self.assertEqual(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]), "mislav")

if __name__ == "__main__":
  unittest.main()