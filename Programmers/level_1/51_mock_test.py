def solution(answers):
    answer = []
    big_num = 0
    one = supo_one(answers)
    two = supo_two(answers)
    three = supo_three(answers)
    big_num = max(big_num, one)
    big_num = max(big_num, two)
    big_num = max(big_num, three)
    if one == big_num:
        answer.append(1)
    if two == big_num:
        answer.append(2)
    if three == big_num:
        answer.append(3)
    return answer

def supo_one(answers):
    answer = 0
    rules = [1, 2, 3, 4, 5]
    for i in range(len(answers)):
        if answers[i] == rules[i % 5]:
            answer += 1
    return answer

def supo_two(answers):
    answer = 0
    rules = [1, 3, 4, 5]
    for i in range(len(answers)):
        if i % 2 == 0:
            if answers[i] == 2:
                answer += 1
        else:
            if answers[i] == rules[(i // 2) % 4]:
                answer += 1
    return answer

def supo_three(answers):
    answer = 0
    rules = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == rules[i % 10]:
            answer += 1
    return answer