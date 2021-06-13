def solution(numbers, hand):
    answer = ""
    coord = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    cl = [0, 3]
    cr = [2, 3]
    for num in numbers:
        if num in coord[0]:
            answer += "L"
            cl = [0, coord[0].index(num)]
        elif num in coord[2]:
            answer += "R"
            cr = [2, coord[2].index(num)]
        else:
            nindex = [1, coord[1].index(num)]
            compl = abs(cl[0] - 1) + abs(cl[1] - nindex[1])
            compr = abs(cr[0] - 1) + abs(cr[1] - nindex[1])
            if compl == compr:
                if hand == "left":
                    answer += "L"
                    cl = nindex
                else:
                    answer += "R"
                    cr = nindex
            if compl > compr:
                answer += "R"
                cr = nindex
            if compl < compr:
                answer += "L"
                cl = nindex

    return answer


number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(number, hand))
