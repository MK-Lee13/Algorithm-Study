import math

def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        if get_value(n) == True:
            answer += n
        else:
            answer -= n
    return answer

def get_value(n):
    mid = int(math.sqrt(n)) 
    return mid * mid != n