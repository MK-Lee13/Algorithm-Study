def solution(s, n):
    if len(s) == 0:
        return s
    
    return shift(s, n)

def shift(s, n):
    result = ""
    shift_num = n % 26
    for _s in s:
        ascii_str = ord(_s)
        if _s == ' ':
            result += _s
            continue
        if ord('z') < ascii_str + shift_num:
            result += chr(ascii_str - 26 + shift_num)
            continue
        if ord('a') > ascii_str and ord('Z') < ascii_str + shift_num:
            result += chr(ascii_str - 26 + shift_num)
            continue
        result += chr(ascii_str + shift_num)
    return result