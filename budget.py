# 1
# 입출력 예만 보고 combinations를 사용했는데 당연히 시간 초과였다
from itertools import combinations


def solution(d, budget):
    a = []
    for i in range(1, len(d) + 1):
        p = list(combinations(d, i))
        r = list(map(len, list(filter(lambda x: sum(x) == budget, p))))
        a.append(r)
    return max(a)[0]


# 2
# 합이 budget보다 큰 경우에는 제일 뒤에 있는 큰 수부터 뺀다
def solution2(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)
