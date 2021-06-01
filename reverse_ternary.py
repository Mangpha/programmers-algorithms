# n에서 3을 계속 나누면 나머지가 나오는데
# 나머지로 문자열을 만들면 문제에서 말한 뒤집힌 3진법의 형태가 나온다
# int(n, base) 3진법이기때문에 int(n, 3)로 return 해주면 된다


def solution(n):
    res = ""
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return int(res, 3)


print(solution(125))
