def solution(n, t, m, timetable):
    time_line = make_shuttle_time_line(n, t)
    timetable_new = get_timetable_new(timetable)
    for i in range(len(time_line) - 1):
        c_time = time_line[i]
        count = 0
        while len(timetable_new) != 0 and timetable_new[0] <= c_time and count < m:
            timetable_new.pop(0)
            count += 1
    
    next_korn = []
    c_time = time_line[-1]
    for i in range(len(timetable_new)):
        if timetable_new[i] <= c_time:
            next_korn.append(timetable_new[i])
        else:
            break
    if len(next_korn) < m:
        return get_time_str(c_time)
    return get_time_str(next_korn[m-1] - 1)

def get_timetable_new(timetable):
    timetable_new = []
    for time in timetable:
        timestamp = get_timestamp(time)
        if timestamp < 24 * 60:
            timetable_new.append(get_timestamp(time))
    timetable_new.sort()
    return timetable_new

def get_timestamp(t_str):
    split_str = t_str.split(":")
    return int(split_str[0]) * 60 + int(split_str[1])

def make_shuttle_time_line(n, t):
    start = 9 * 60
    time_line = []
    for i in range(n):
        time_line.append(start)
        start += t
    return time_line

def get_time_str(timestamp):
    h = timestamp // 60
    m = timestamp % 60
    str_h = str(h)
    str_m = str(m)
    if h < 10:
        str_h = "0" + str_h
    if m < 10:
        str_m = "0" + str_m
    return f"{str_h}:{str_m}"