def solution(numbers):
    answer = {}
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer[numbers[i] + numbers[j]] = 0
    result = list(answer.keys())
    result.sort()
    return result