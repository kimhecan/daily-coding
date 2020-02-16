import unittest

def solution(s):
  splitArr = s.split(" ")
  prevAnswer = []
  for string in splitArr:
    tempStr = ""
    for j, v in enumerate(list(string)):
      if j % 2 == 0: tempStr += v.upper()
      if j % 2 != 0: tempStr += v.lower()
    prevAnswer.append(tempStr)
  return " ".join(prevAnswer)
  # return " ".join(list(map(lambda x: "".join(list(map(lambda y: y.upper() if x.index(y) % 2 == 0 else y.lower(), x))), splitArr)))
  # return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution("try hello world"), "TrY HeLlO WoRlD")



if __name__ == '__main__':
    unittest.main()
    