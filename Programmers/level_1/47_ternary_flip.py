def solution(n):
    answer = 0
    notation_str = get_k_notation(3, n)
    notation_count = 0
    for _str in notation_str:
        notation_num = int(_str)
        if notation_num != 0:
            answer += notation_num * (3 ** notation_count)
        notation_count += 1
    return answer

def get_k_notation(k, n):
    notation_str = ""
    while n > 0:
        notation_str += str(n % k)
        n = n // k
    return notation_str[::-1]