# 1
# left와 right 범위를 구해서 그 사이값 전부 약수를 구해서
# 짝수인지 홀수인지 확인하는 코드로 실행했다


def solution(left, right):
    arr = [i for i in range(left, right + 1)]
    for j in range(len(arr)):
        c = 0
        for k in range(1, arr[j] + 1):
            if arr[j] % k == 0:
                c += 1
        if c % 2 != 0:
            arr[j] = -arr[j]

    return sum(arr)


# 2
# 다른 분 풀이를 보다가 약수의 개수는 4, 9, ..와 같이 n ** 0.5가 딱 떨어지는 수가 아니면
# 전부 짝수개인걸 알았다..
# 그리고 불필요하다고 생각된 코드들을 정리했다
def solution2(left, right):
    res = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            res -= i
        else:
            res += i
    return res
