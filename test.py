import collections


def solutionWithCollection(participant, completion):
    obj = collections.Counter(participant) - collections.Counter(completion)
    return list(obj)[0]


print(solutionWithCollection(['mislav', 'stanko', 'mislav', 'ana'], [
    'stanko', 'ana', 'mislav']))


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
