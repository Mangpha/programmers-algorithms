# 정렬해서 인용횟수가 인덱스보다 작아지는 경우까지 찾는다


def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)


print(solution([4, 0, 1, 6, 7, 12]))
