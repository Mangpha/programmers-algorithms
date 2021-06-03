# filter와 lambda를 사용해서 배열을 바꿔서 리턴해주면 된다.


def solution(arr, divisor):
    answer = list(filter(lambda x: x % divisor == 0, arr))
    if len(answer) == 0:
        return [-1]
    return answer


print(solution([5, 9, 7, 10], 5))
