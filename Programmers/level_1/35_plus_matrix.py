def solution(arr1, arr2):
    answer = make_answer(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

def make_answer(arr):
    return [[0] * len(arr[i]) for i in range(len(arr))]