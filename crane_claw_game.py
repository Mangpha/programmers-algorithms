# 처음에 문제 이해를 못해서 엄청 힘들었다.
# 그러다가 공책에 몇번 끄적여보니 보였다.


def solution(board, moves):
    dummy = []
    ans = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                dummy.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                if dummy[-1:] == dummy[-2:-1]:
                    dummy.pop()
                    dummy.pop()
                    ans += 2
                break
    return ans


solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4],
)
