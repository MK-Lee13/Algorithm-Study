def solution(enter, leave):
    answer = []
    answer_map = make_match_map(enter)
    for i in range(len(leave)):
        next_leave = leave[i]
        leave_index = i
        enter_index = enter.index(next_leave)
        for j in range(enter_index):
            answer_map[next_leave].add(enter[j])
            answer_map[enter[j]].add(next_leave)
            insert_list(enter[:enter_index], answer_map, enter[j])
        enter.pop(enter_index)
    return [ len(answer_map[i]) for i in range(1, len(leave) + 1) ]

def insert_list(part_list, answer_map, enter_value):
    for part in part_list:
        if enter_value == part:
            continue
        answer_map[enter_value].add(part)

def make_match_map(enter):
    result = {}
    for i in range(1, len(enter) + 1):
        result[i] = set()
    return result