import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2:
        m = heapq.heappop(scoville)
        if m >= K:
            return count
        sm = heapq.heappop(scoville)
        heapq.heappush(scoville, m + sm * 2)
        count += 1
    if scoville[0] >= K:
        return count
    return -1


# 테스트 케이스
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)