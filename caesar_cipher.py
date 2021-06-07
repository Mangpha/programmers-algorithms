# 대문자는 65~90, 소문자는 97~122
# 범위 밖인 수가 나오면 그 범위의 첫 부분으로 이동한다. 코드 12, 17번째줄


def solution(s, n):
    r = ""
    for i in list(s):
        if i == " ":
            r += " "
        i = ord(i)
        if i >= 65 and i <= 90:
            if i + n > 90:
                r += chr(i - 26 + n)
            else:
                r += chr(i + n)
        if i >= 97 and i <= 122:
            if i + n > 122:
                r += chr(i - 26 + n)
            else:
                r += chr(i + n)

    return r


print(solution("AB", 1))
