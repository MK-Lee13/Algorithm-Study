def solution(rows, columns, queries):
    answer = []
    maps = make_map(rows, columns)
    for query in queries:
        answer.append(hurricane(maps, query))
    return answer

def make_map(rows, columns):
    maps = []
    count = 1
    for i in range(rows):
        col = []
        for j in range(columns):
            col.append(count)
            count += 1
        maps.append(col)
    return maps

def hurricane(maps, query):
    change_list = []
    y1, x1, y2, x2 = query
    next_move_element = maps[y1 - 1][x1 - 1]
    change_list.append(next_move_element)
    for i1 in range(x1, x2):
        tmp_next_move_element = maps[y1 - 1][i1]
        maps[y1 - 1][i1] = next_move_element
        next_move_element = tmp_next_move_element
        change_list.append(next_move_element)
    for i2 in range(y1, y2):
        tmp_next_move_element = maps[i2][x2 - 1]
        maps[i2][x2 - 1] = next_move_element
        next_move_element = tmp_next_move_element
        change_list.append(next_move_element)
    for i3 in range(x2 - 2, x1 - 2, -1):
        tmp_next_move_element = maps[y2 - 1][i3]
        maps[y2 - 1][i3] = next_move_element
        next_move_element = tmp_next_move_element
        change_list.append(next_move_element)
    for i4 in range(y2 - 2, y1 - 1, -1):
        tmp_next_move_element = maps[i4][x1 - 1]
        maps[i4][x1 - 1] = next_move_element
        next_move_element = tmp_next_move_element
        change_list.append(next_move_element)
    maps[y1 - 1][x1 - 1] = next_move_element
    return min(change_list)
    