def solution(s):
    answer = True
    matcher = {
        "p" : 0,
        "P" : 0,
        "y" : 1,
        "Y" : 1
    }
    p = 0
    y = 0
    for c in s:
        if c not in matcher:
            continue
        if matcher[c] == 1:
            y += 1
        else:
            p += 1

    return p == y