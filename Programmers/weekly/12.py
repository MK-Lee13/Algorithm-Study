from itertools import permutations

def solution(k, dungeons):
    answer = -1
    dungeon_map = [i for i in range(len(dungeons))]
    result = list(permutations(dungeon_map, len(dungeons)))
    
    for res in result:
        loop_max = get_max(res, k, dungeons)
        if loop_max == len(dungeons):
            return loop_max
        if loop_max > answer:
            answer = loop_max
    return answer

def get_max(res, k, dungeons):
    result = 0
    for loop in res:
        min_p, nes_p = dungeons[loop]
        if k < min_p:
            break
        result += 1
        k -= nes_p
    return result