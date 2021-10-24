def solution(numbers, hand):
    key_pad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1]
    }
    start_left = [3, 0]
    start_right = [3, 2]
    answer = ''
    for number in numbers:
        position = key_pad[number]
        
        if position[1] == 0:
            answer += "L"
            start_left = position
            continue
        elif position[1] == 2:
            answer += "R"
            start_right = position
            continue
            
        left_length = get_length(start_left, position)
        right_length = get_length(start_right, position)
        
        if left_length > right_length:
            answer += "R"
            start_right = position
        elif left_length < right_length:
            answer += "L"
            start_left = position
        elif hand == "right":
            answer += "R"
            start_right = position
        else:
            answer += "L"
            start_left = position
    return answer

def get_length(start, click):
    x = start[0] - click[0]
    y = start[1] - click[1]
    if x < 0: 
        x = -x
    if y < 0:
        y = -y
    return x + y