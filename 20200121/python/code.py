import unittest
import collections


def solutionWithCollection(participant, completion):
    obj = collections.Counter(participant) - collections.Counter(completion)
    return list(obj)[0]


solutionWithCollection(['mislav', 'stanko', 'mislav', 'ana'], [
    'stanko', 'ana', 'mislav'])


def solution(participant, completion):
    partiObj = {}
    for i in participant:
        partiObj[i] = 0

    for i in participant:
        partiObj[i] += 1

    for i in completion:
        partiObj[i] -= 1

    for i in partiObj:
        if partiObj[i] == 1:
            return i


solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])


class MyTests(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(
            solution(["leo", "kiki", "eden"], ["eden", "kiki"]), "leo")

    def test_solution2(self):
        self.assertEqual(solution(["marina", "josipa", "nikola", "vinko", "filipa"]	, [
                         "josipa", "filipa", "marina", "nikola"]), "vinko")

    def test_solution3(self):
        self.assertEqual(solution(["mislav", "stanko", "mislav", "ana"], [
                         "stanko", "ana", "mislav"]), "mislav")


if __name__ == "__main__":
    unittest.main()
