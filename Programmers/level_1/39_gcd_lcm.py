def solution(n, m):
    answer = []
    l = gcd(n, m)
    answer.append(l)
    answer.append((n * m) // l)
    return answer


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b