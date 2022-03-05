def solution(land):
    answer = 0
    last_index = len(land) - 1
    for i in range(1, len(land)):
        land[i][0] += get_max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += get_max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += get_max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += get_max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
    return get_answer(land[last_index])

def get_answer(last_arr):
    max_num = 0
    for arr in last_arr:
        max_num = max(max_num, arr)
    return max_num

def get_max(a, b, c):
    max_num = a
    max_num = max(max_num, b)
    max_num = max(max_num, c)
    return max_num
    