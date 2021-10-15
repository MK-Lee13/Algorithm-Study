def solution(lottos, win_nums):
    max_win = 0
    min_win = 0
    
    for lotto in lottos:
        if lotto == 0:
            max_win += 1
            continue
        if lotto in win_nums:
            max_win += 1
            min_win += 1
    
    max_score = 7 - max_win
    min_score = 7 - min_win
    
    if min_score > 6:
        min_score = 6
    if max_score > 6:
        max_score = 6
    return [max_score, min_score]