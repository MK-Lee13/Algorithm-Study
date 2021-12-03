def solution(s):
    answer = ''
    list_s = list(s)
    list_answer = sorted(list_s, key = lambda x : (-ord_maker(x[0])))
    return "".join(list_answer)

def ord_maker(x):
    s_num = ord(x)
    return s_num