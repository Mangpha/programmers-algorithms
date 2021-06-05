def solution(s):
    p = len(list(filter(lambda x: x == "p", s.lower())))
    y = len(list(filter(lambda x: x == "y", s.lower())))

    return p == y


print(solution("pPoooyY"))
