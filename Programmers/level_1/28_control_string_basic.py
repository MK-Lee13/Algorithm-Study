def solution(s):
    num = {"0":1,"1":1,"2":1,"3":1,"4":1,"5":1,"6":1,"7":1,"8":1,"9":1}
    if len(s) != 4 and len(s) != 6:
        return False
    for c in s:
        if c not in num:
            return False
    return True