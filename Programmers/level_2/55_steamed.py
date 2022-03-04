def solution(msg):
    answer = []
    index_map = init_index_map()
    index_map_count = 27
    if len(msg) == 1:
        return [index_map[msg]]
    
    next_index = 1
    end_index = len(msg)
    w = msg[0]
    c = msg[1]
    
    while next_index < end_index - 1:
        if (w + c) in index_map:
            next_index += 1
            w += c
            c = msg[next_index]
            continue
        answer.append(index_map[w])
        index_map[(w + c)] = index_map_count
        index_map_count += 1
        next_index += 1
        w = c
        c = msg[next_index]
    if (w + c) in index_map:
        answer.append(index_map[(w + c)])
    else:
        answer.append(index_map[w])
        answer.append(index_map[c])
        
    return answer

def init_index_map():
    index_map = {}
    next_index = ord('A')
    for i in range(1, 27):
        index_map[chr(next_index)] = i
        next_index += 1
    return index_map