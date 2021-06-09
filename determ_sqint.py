from math import ceil


def solution(n):
    return (int(n ** 0.5) + 1) ** 2 if n ** 0.5 == ceil(n ** 0.5) else -1


print(solution(121))
