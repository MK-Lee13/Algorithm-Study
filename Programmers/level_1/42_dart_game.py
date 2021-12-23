def solution(dartResult):
    answer = 0
    score_list = []
    current_score_str = ""
    current_score = 0
    for dart in dartResult:
        if dart == "S":
            current_score = get_current_score(current_score, current_score_str)
        elif dart == "D":
            current_score = get_current_score(current_score, current_score_str)
            current_score **= 2
        elif dart == "T":
            current_score = get_current_score(current_score, current_score_str)
            current_score **= 3
        elif dart == "*":
            current_score = get_current_score(current_score, current_score_str)
            current_score *= 2
            if len(score_list) != 0:
                score_list[-1] = score_list[-1] * 2 
        elif dart == "#":
            current_score = get_current_score(current_score, current_score_str)
            current_score *= -1
        else:
            current_score_str += dart
            if current_score != 0:
                score_list.append(current_score)
                current_score = 0
                current_score_str = dart
                
    if current_score != 0:
        score_list.append(current_score)
        
    return sum(score_list)

def get_current_score(current_score, current_score_str):
    if current_score != 0:
        return current_score
    return int(current_score_str)
    