# 1


def solution(participant, completion):
    for i in range(len(completion)):
        if completion[i] in participant:
            participant.remove(completion[i])
    return "".join(participant)


# 2

from collections import Counter


def solution2(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]


p1 = ["mislav", "stanko", "mislav", "ana"]
c1 = ["stanko", "ana", "mislav"]
