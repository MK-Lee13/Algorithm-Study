from itertools import combinations

def solution(orders, course):
    answer_dict = {}
    for plate in orders:
        for i in range(2, len(plate) + 1):
            comb = list(combinations(plate, i))
            for c in comb:
                a = list(c)
                a.sort()
                key = "".join(a)
                if key in answer_dict:
                    answer_dict[key] += 1
                else:
                    answer_dict[key] = 1
    answer = []
    # print(answer_dict)
    for count in course:
        answer += find(count, answer_dict)
    answer.sort()
    return answer

def find(count, answer_dict):
    result = []
    count_list = []
    max_val = 2
    for key in answer_dict:
        if count != len(key):
            continue
        if answer_dict[key] >= 2:
            count_list.append([key, answer_dict[key]])
        if answer_dict[key] > max_val:
            max_val = answer_dict[key]
    for cnt in count_list:
        if cnt[1] == max_val:
            result.append(cnt[0])
    return result