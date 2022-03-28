from collections import deque

def solution(arr):
    isValid, val = compare([0, len(arr), 0, len(arr)], arr)
    if isValid == True:
        if val == 0:
            return [1, 0]
        else:
            return [0, 1]
    answer = compress(arr)
    zero = answer.count(0)
    one = answer.count(1)
    return [zero, one]

def compress(arr):
    result = []
    divide_queue = deque()
    divide_append(divide(0, len(arr), 0, len(arr)), divide_queue)
    while divide_queue:
        data = divide_queue.popleft()
        x1, x2, y1, y2 = data
        if x2 - x1 <= 1:
            result.append(arr[y1][x1])
            continue
        isValid, val = compare(data, arr)
        if isValid == True:
            result.append(val)
        else:
            divide_append(divide(data[0], data[1], data[2], data[3]), divide_queue)
    return result

def divide_append(divide_data, divide_queue):
    for divide_one in divide_data:
        divide_queue.append(divide_one)
        
def divide(x1, x2, y1, y2):
    result = []
    half_len = (x2 - x1) // 2
    result.append([x1, x1 + half_len, y1, y1 + half_len])
    result.append([x1 + half_len, x2, y1, y1 + half_len])
    result.append([x1, x1 + half_len, y1 + half_len, y2])
    result.append([x1 + half_len, x2, y1 + half_len, y2])
    return result

def compare(data, arr):
    x1, x2, y1, y2 = data
    zero_count = 0
    one_count = 0
    for y in range(y1, y2):
        for x in range(x1, x2):
            if arr[y][x] == 0:
                zero_count += 1
            if arr[y][x] == 1:
                one_count += 1
            if zero_count != 0 and one_count != 0:
                return False, -1
    if zero_count == 0:
        return True, 1
    return True, 0
    
    