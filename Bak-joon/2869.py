import math

def to_input():
    a, b, v = [ int(w) for w in input().split() ]
    return a, b, v

def solution(a, b, v):
    # 무조건 1일차에 해결할 수 있는 경우
    if a >= v:
        return 1
    '''
    정상에 올라간 후에 미끄러지지 않는다는 제약조건
    이 있기 때문에 가장 먼저 v - a 값 (오전에 올라갈 수 있는 경우)에
    a - b 값 (오전, 오후 다 합해서 그 하루에 올라갈 수 있는 층수)을 나누어서 계산한다
    '''
    if_upper = v - a
    up_value = a - b

    is_case = math.ceil(if_upper / up_value)
    return is_case + 1

a, b, v = to_input()
print(solution(a, b, v))