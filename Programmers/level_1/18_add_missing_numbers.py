def solution(numbers):
    answer = 0
    check_sum = make_map()
    for num in numbers:
        check_sum[num] += 1
    for key in check_sum:
        if check_sum[key] == 0:
            answer += key
    return answer

def make_map():
    result = {}
    for i in range(10):
        result[i] = 0
    return result