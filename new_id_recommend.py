# 정규식에 대해서 좀 더 공부해볼 수 있는 시간이 되었다
import re


def solution(new_id):
    # 소문자처리, 영어, 숫자, 일부 특수문자 제외 제거
    new_id = re.sub("[^a-z0-9\-._]", "", new_id.lower())
    # . => 2번 이상 연속된 부분 치환
    new_id = re.sub("\.+", ".", new_id)
    # . => 처음이나 마지막에 위치할 경우 제거
    new_id = re.sub("^\.|\.$", "", new_id)
    # new_id의 길이가 0인 경우
    if len(new_id) == 0:
        new_id = "a"
    # new_id 16자리 이상인경우 0:15 slice
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    # 마지막 문자가 . 인경우 제거
    new_id = re.sub("\.$", "", new_id)
    # new_id의 길이가 2이하 인경우
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
