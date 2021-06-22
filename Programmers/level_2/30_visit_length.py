def solution(dirs):
    on_map = {}
    x_pos = 5
    y_pos = 5
    
    for dir_ in dirs:
        if dir_ == "L" and x_pos != 0:
            on_map[f"{x_pos - 1}, {y_pos}, {x_pos}, {y_pos}"]  = 1
            x_pos -= 1
        elif dir_ == "R" and x_pos != 10:
            on_map[f"{x_pos}, {y_pos}, {x_pos + 1}, {y_pos}"]  = 1
            x_pos += 1
        elif dir_ == "D" and y_pos != 0:
            on_map[f"{x_pos}, {y_pos - 1}, {x_pos}, {y_pos}"]  = 1
            y_pos -= 1
        elif dir_ == "U" and y_pos != 10:
            on_map[f"{x_pos}, {y_pos}, {x_pos}, {y_pos + 1}"]  = 1
            y_pos += 1
    
    return len(on_map) 