def solution(n):
    vers = 2
    while n % vers != 1:
        vers += 1
    return vers