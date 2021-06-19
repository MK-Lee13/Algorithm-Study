from itertools import product

def solution(user_id, banned_id):
    answer = 1
    permute = init_dict(banned_id)
    
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if check_id(user_id[j], banned_id[i]) == True:
                permute[i].append(j)
    # print(permute)
    result = []
    for key in permute:
        result.append(permute[key])
    # print(result)
    prod = list(product(*result))
    prod_tuples = []
    for pr in prod:
        set_ = set(list(pr))
        if len(set_) == len(banned_id):
            prod_tuples.append(list(pr))
    prod_list = list(set([tuple(set(prod_tuple)) for prod_tuple in prod_tuples]) )
    return len(prod_list)

def init_dict(banned_id):
    result = {}
    for i in range(len(banned_id)):
        result[i] = []
    return result

def check_id(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(len(user)):
        if ban[i] == "*":
            continue
        if ban[i] != user[i]:
            return False
    return True