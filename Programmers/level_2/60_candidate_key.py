from itertools import combinations

def solution(relation):
    answer = []
    tuple_len = len(relation[0])
    unique_len = len(relation)
    keys = make_keys(tuple_len)
    for i in range(1, tuple_len + 1):
        combination = list(combinations(keys, i))
        for key_list in combination:
            relation_map = make_relation_map(relation, key_list)
            if check_map(relation_map, unique_len) == True and is_minimal(answer, key_list) == True:
                answer.append(recombine_key_list(key_list))
    return len(answer)

def recombine_key_list(key_list):
    new_key_list = []
    for key in key_list:
        new_key_list.append(key)
    return new_key_list

def is_minimal(answer, key_list):
    for ans in answer:
        count = 0
        for u_key in ans:
            if u_key in key_list:
                count += 1
        if len(ans) == count:
            return False
    return True

def make_keys(tuple_len):
    return [i for i in range(tuple_len)]

def check_map(relation_map, unique_len):
    if unique_len == len(relation_map):
        return True
    return False

def make_relation_map(relation, key_list):
    relation_map = {}
    for tp in relation:
        key_set = ""
        for key in key_list:
            key_set += str(tp[key])
        relation_map[key_set] = 1
    return relation_map