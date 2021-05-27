def solution(abolutes, signs):
    arr = list(zip(abolutes, signs))
    res = []
    for x, y in arr:
        if y is True:
            res.append(+x)
        else:
            res.append(-x)
    return sum(res)


ab = [4, 7, 12]
sign = [True, False, True]
print(solution(ab, sign))
