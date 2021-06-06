# permutations를 이용해서 2개씩 더한값을 정렬하고 중복을 제거한다

from itertools import permutations


def solution(numbers):
    answer = list(permutations(set(numbers), 2))
    answer = list(map(lambda x: sum(x), answer))

    return sorted(list(set(answer)))


print(solution([5, 0, 2, 7]))
