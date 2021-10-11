def solution(n):
    answer = []
    maps, total_count = init_map(n)
    count = 0
    loop_count = 0
    while count < total_count:
        count += set_col_start(maps, count + 1, loop_count)
        count += set_row_last(maps, count + 1, loop_count)
        count += set_col_last(maps, count + 1, loop_count)
        loop_count += 1
    return get_answer(maps)

def get_answer(maps):
    answer = []
    for mp in maps:
        answer += [w for w in mp]
    return answer

def init_map(n):
    result = []
    total_count = 0
    for i in range(n):
        col = []
        col.append(0)
        total_count += 1
        for j in range(i):
            col.append(0)
            total_count += 1
        result.append(col)
    return result, total_count

def set_col_start(maps, start_value, loop_count):
    plus_count = 0
    for i in range(loop_count, len(maps) - loop_count):
        if maps[i][loop_count] != 0:
            continue
        maps[i][loop_count] = start_value + plus_count
        plus_count += 1
    return plus_count

def set_col_last(maps, start_value, loop_count):
    plus_count = 0
    for i in range(len(maps) - (loop_count + 2), loop_count, -1):
        last_index = len(maps[i]) - 1 - loop_count
        if maps[i][last_index] != 0:
            continue
        maps[i][last_index] = start_value + plus_count
        plus_count += 1
    return plus_count

def set_row_last(maps, start_value, loop_count):
    plus_count = 0
    last_index = (len(maps) - 1) - loop_count 
    for i in range(loop_count + 1, last_index + 1):
        if maps[last_index][i] != 0:
            continue
        maps[last_index][i] = start_value + plus_count
        plus_count += 1
    return plus_count