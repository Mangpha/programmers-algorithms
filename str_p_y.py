# filter로 p가 들어있는 배열의 길이와 y가 들어있는 배열의 길이를 비교한다


def solution(s):
    p = len(list(filter(lambda x: x == "p", s.lower())))
    y = len(list(filter(lambda x: x == "y", s.lower())))

    return p == y


print(solution("pPoooyY"))
