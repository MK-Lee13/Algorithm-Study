def solution(x):
    num = x
    shard = 0
    while x != 0:
        shard += x % 10
        x //= 10
    if num % shard != 0:
        return False
    return True