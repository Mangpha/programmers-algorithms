def solution(numbers, target):
    q = [0]
    for num in numbers:
        buf = []
        for i in range(len(q)):
            j = q.pop()
            buf.append(j + num)
            buf.append(j - num)
        q = buf.copy()
    return q.count(target)


solution([1, 1, 1, 1, 1], 3)
