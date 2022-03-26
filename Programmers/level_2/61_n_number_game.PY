num_list = [
    "0", "1", "2", "3", "4", "5", "6"
    , "7", "8", "9", "A", "B", "C", "D"
    , "E", "F"
]

def solution(n, t, m, p):
    answer = ""
    f_str = make_full_string_list(t, m, n, p)
    for i in range(t):
        new_i = (i * m) + p
        answer += f_str[new_i - 1]
    return answer

def make_full_string_list(t, m, n, p):
    answer = ""
    for num in range(0, (t * m + p)):
        answer += get_k_notation(n, num)
    return answer

def get_k_notation(k, n):
    notation_str = ""
    if n == 0:
        return "0"
    while n > 0:
        notation_str += num_list[n % k]
        n = n // k
    return notation_str[::-1]