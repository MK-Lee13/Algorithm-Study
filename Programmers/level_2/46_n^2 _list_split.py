def solution(n, left, right):
    answer = []
    n_two_list = make_list(n, left, right)
    return n_two_list

def make_list(n, left, right):
    n_two_list = []
    count = right - left + 1
    
    start_y = 0
    start_x = 0
    next_div = left
    if next_div != 0:
        start_y = next_div // n
        start_x = next_div % n
    
    while count > 0:
        if start_y > start_x:
            n_two_list.append(start_y + 1)
        else:
            n_two_list.append(start_x + 1)
        count -= 1
        next_div += 1
        start_y = next_div // n
        start_x = next_div % n
        
    return n_two_list