def solution(id_list, report, k):
    answer = []
    declare_map, id_map = init_maps(id_list)
    for rp in report:
        split_rp = rp.split(" ")
        declare_map[split_rp[1]].add(split_rp[0])
        id_map[split_rp[0]].add(split_rp[1])
    
    for id_key in id_map:
        count = 0
        for d_key in id_map[id_key]:
            if len(declare_map[d_key]) >= k:
                count += 1
        answer.append(count)
    return answer

def init_maps(id_list):
    declare_map = {}
    id_map = {}
    for _id in id_list:
        declare_map[_id] = set()
        id_map[_id] = set()
    return declare_map, id_map