# 문자열을 sort하면 차례대로 정렬이 되기때문에 sort하고
# 첫번째 문자를 뺀 배열과 검사했다


def solution(phone_book):
    phone_book.sort()
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True
