import itertools


def checking(nums):
    if nums == 0 or nums == 1:
        return False
    for i in range(2, int(nums ** (0.5)) + 1):

        if nums % i == 0:
            return False

    return True


def solution(nums):
    res = list(itertools.combinations(nums, 3))
    arr = 0
    for i in res:
        sm = sum(i)
        if checking(sm):
            arr += 1

    return arr


num = [1, 2, 7, 6, 4]
print(solution(num))
