from datetime import date

week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

def solution(a, b):
    index = date(2016, a, b).weekday()
    return week[index]