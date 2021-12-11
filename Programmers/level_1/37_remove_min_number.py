def solution(arr):
    answer = []
    if len(arr) < 2:
        return [-1]
    min_el = arr[0]
    min_index = 0
    for i in range(len(arr)):
        el = arr[i]
        if el < min_el:
            min_el = el
            min_index = i
    arr.pop(min_index)
    return arr