# list slice


def solution1(array, commands):
    return [
        sorted(array[commands[i][0] - 1 : commands[i][1]])[commands[i][2] - 1]
        for i in range(len(commands))
    ]


# commands 길이를 range로 줄 필요가 없어보였다


def solution2(array, commands):
    return [sorted(array[c[0] - 1 : c[1]])[c[2] - 1] for c in commands]
