from collections import deque

def solution(n, results):
    answer = 0
    down_map = {}
    up_map = {}
    for score in results:
        set_down_score_map(down_map, score)
        set_up_score_map(up_map, score)
    for target in range(1, n + 1):
        if is_valid(target, up_map, down_map, n) == True:
            answer += 1
    return answer

def is_valid(target, up_map, down_map, n):
    valid_name = [target]
    if target in up_map:
        up_check(target, up_map, valid_name)
    if target in down_map:
        down_check(target, down_map, valid_name)
    return n == len(valid_name)
    
def up_check(target, up_map, valid_name):
    queue = deque()
    queue.append(target)
    while queue:
        c_name = queue.popleft()
        if c_name not in up_map:
            continue
        for key in up_map[c_name]:
            if key not in valid_name:
                queue.append(key)
                valid_name.append(key)
    
def down_check(target, down_map, valid_name):
    queue = deque()
    queue.append(target)
    while queue:
        c_name = queue.popleft()
        if c_name not in down_map:
            continue
        for key in down_map[c_name]:
            if key not in valid_name:
                queue.append(key)
                valid_name.append(key)
    

def set_down_score_map(down_map, score):
    win = score[0]
    loose = score[1]
    if loose in down_map:
        down_map[loose][win] = 1
    else:
        down_map[loose] = {}
        down_map[loose][win] = 1

def set_up_score_map(up_map, score):
    win = score[0]
    loose = score[1]
    if win in up_map:
        up_map[win][loose] = 1
    else:
        up_map[win] = {}
        up_map[win][loose] = 1