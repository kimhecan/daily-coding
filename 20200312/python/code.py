import unittest
import re

def solution(n, arr1, arr2):
    return [ re.sub('0|1', 
                   lambda v: "#" if int(v.group()) else " ",
                   '0' * (n - len(bin(arr1[i]|arr2[i])[2:])) + bin(arr1[i]|arr2[i])[2:]) for i in range(0, n)
                  ]



class MyTest(unittest.TestCase):
  def test_solution1(self):
    self.assertEqual(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]), ["######", "###  #", "##  ##", " #### ", " #####", "### # "])
  
  def test_solution2(self):
    self.assertEqual(solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28]), ["#####","# # #", "### #", "#  ##", "#####"])
    

if __name__ == "__main__":
    unittest.main()

