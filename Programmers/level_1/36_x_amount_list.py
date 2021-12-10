def solution(x, n):
    answer = []
    next_ans = x
    for i in range(n):
        answer.append(next_ans)
        next_ans += x
    return answer