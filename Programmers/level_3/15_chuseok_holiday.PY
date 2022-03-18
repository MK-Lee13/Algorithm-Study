import math
s = 1
m = s * 60
h = m * 60

def solution(lines):
    answer = 1
    s_map = {}
    pair = []
    for line in lines:
        end, start = get_time_delta(line)
        pair.append([start, end])
    for i in range(len(pair)):
        c_answer = 1
        for j in range(i + 1, len(pair)):
            if pair[i][1] + 1 > pair[j][0]:
                c_answer += 1
        if c_answer > answer:
            answer = c_answer
    return answer

def get_time_delta(time_str):
    split_time_str = time_str.split(" ")
    transaction = float(split_time_str[2][:-1])
    time_delta = get_hour_time_delta(split_time_str[1])
    return time_delta, time_delta - transaction + 0.001

def get_hour_time_delta(hour):
    time_delta = 0
    sp_hour = hour.split(":")
    time_delta += int(sp_hour[0]) * h
    time_delta += int(sp_hour[1]) * m
    time_delta += float(sp_hour[2])
    return time_delta