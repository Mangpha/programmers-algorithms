# 1
# 약수를 이용해서 코딩
# 채점했을때 정답이긴 했지만
# 코드가 너무 길어져서 다시 코딩


def ck(num):
    p_num = []
    p_num_back = []
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            p_num.append(i)
            if i != (num // i):
                p_num_back.append(num // i)
            if i == (num // i):
                p_num_back.append(i)

    return list(zip(p_num, p_num_back))


def solution1(brown, yellow):
    for i, j in ck(yellow):
        # 이 부분은 처음에 그림을 그려보면서 생각하다가 찾았다
        if brown == ((i * 2) + (j * 2) + 4):
            b = max(i, j) + 2
            y = min(i, j) + 2
            return [b, y]


# 2
# 굳이 다른 배열에 넣을 필요가 없다고 생각됨
# 위에서 했던 약수를 이용해서 가로 길이와 세로 길이를 구한다


def solution2(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            if (brown - 4) == (i * 2) + ((yellow // i) * 2):
                # 가로 길이가 더 길다
                return [(yellow // i) + 2, i + 2]


print(solution2(24, 24))
