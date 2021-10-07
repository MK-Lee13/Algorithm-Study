def gcd(a, b):
    if b > a:
        tmp = a
        a = b
        b = tmp
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b

def solution(arr):
    answer = 0
    a = 0
    b = arr[0]
    for i in range(1, len(arr)):
        a = arr[i]
        c = gcd(a, b)
        b = (a * b) // c
    return b