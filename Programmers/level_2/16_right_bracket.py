def solution(s):
    answer = True
    slot = 0
    for sl in s:
        if sl == '(':
            slot += 1
        else:
            slot -= 1
        
        if slot < 0:
            return False
    if slot != 0:
            return False
        
    return True