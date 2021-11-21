def solution(a, b):
    answer = a + b
    if a > b:
        a, b = b, a
    if a == b:
        answer = a
    for i in range(a + 1, b):
        answer += i
    return answer