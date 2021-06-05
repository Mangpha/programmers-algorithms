# datetime.date(날짜).weekday() => days 인덱스 값으로 리턴

import datetime


def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return days[datetime.date(2016, a, b).weekday()]
