def solution(n):
    compare_bit_count = count_bit(n)
    next_number = n + 1
    while(compare_bit_count != count_bit(next_number)):
        next_number += 1
    return next_number

def count_bit(n):
    count = 0
    while n > 1:
        if n % 2 != 0:
            count += 1
        n //= 2
    if n == 1:
        count += 1
    return count