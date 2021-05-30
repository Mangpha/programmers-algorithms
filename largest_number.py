# 1
# permutations를 이용해서 조합을 만들어서 최댓값을 구하는 방법으로 해봤다
# 하지만 시간 초과로 실패
from itertools import permutations


def solution(numbers):
    lists = list(permutations(numbers, len(numbers)))
    res = []
    for i in lists:
        res.append("".join([str(i[j]) for j in range(len(i))]))
    return max(res)


# 2
# 구글링하다가 문자열 비교와 lambda에 대해서 공부를 했다
# key를 lambda i: i로 했는데 [3, 30] => 330이 아니라 303으로 나왔다
# number의 원소가 1000 이하기 때문에 3자릿수가 나올 수도 있기때문에 문자열을 3번 반복해서 정렬한다
# 0이 여러 번 나올 수 있으니 int로 바꿨다가 다시 str로 바꾼다
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda i: i * 3, reverse=True)
    return str(int("".join(numbers)))


print(solution2([3, 30, 34, 5, 9]))
