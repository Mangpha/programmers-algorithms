from collections import Counter


def solution(lottos, win_nums):
    r = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    user = Counter(lottos)
    z = user[0]
    win = Counter(win_nums)

    return [r[len(user & win) + z], r[len(user & win)]]
