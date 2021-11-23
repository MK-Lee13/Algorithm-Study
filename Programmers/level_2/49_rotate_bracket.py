def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if is_correct(s) == True:
            answer += 1
    return answer

def is_correct(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
            continue
        elif c == "{":
            stack.append(c)
            continue
        elif c == "[":
            stack.append(c)
            continue
        if len(stack) == 0:
            return False
        el = stack.pop()
        if el == "(" and c == ")":
            continue
        elif el == "{" and c == "}":
            continue
        elif el == "[" and c == "]":
            continue
        return False
    if len(stack) != 0 :
        return False
    return True