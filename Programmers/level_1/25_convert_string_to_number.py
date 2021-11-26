def solution(s):
    answer = 0
    role = 1
    num_str = ""
    for c in s:
        if c == "-":
            answer += make_str_num(num_str, role)
            num_str = ""
            role = -1
            answer += make_str_num(num_str, role)
        elif c == "+":
            num_str = ""
            role = 1
        else:
            num_str += c
    answer += make_str_num(num_str, role)
    return answer

def make_str_num(num_str, role):
    if num_str == "":
        return 0
    return int(num_str) * role