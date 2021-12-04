def solution(s):
    answer = ''
    index = 0
    for c in s:
        if c.isalpha() == False:
            answer += c
            index = 0
            continue
        if index % 2 == 0:
            answer += c.upper()
        else:
            answer += c.lower()
        index += 1
    return answer