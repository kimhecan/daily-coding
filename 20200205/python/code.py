import unittest
import datetime

def solution(a, b):
    dayList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return dayList[datetime.date(2016, a, b).weekday()]



class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(1,1), "FRI")

  def test_solution2(self):
    self.assertEqual(solution(5,24), "TUE")


if __name__ == "__main__":
    unittest.main()