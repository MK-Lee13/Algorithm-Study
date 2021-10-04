def solution(sizes):
    answer = 0
    x = 0
    y = 0
    for size in sizes:
        x_axes, y_axes, new_x, new_y = sort_value(x, y, size[0], size[1])
        x = x_axes
        y = y_axes
        if x >= new_x and y >= new_y:
            continue
        if y >= new_x and x >= new_y:
            continue
        if new_x > x:
            x = new_x
        if new_y > y:
            y = new_y
    return x * y

def sort_value(x_axes, y_axes, new_x, new_y):
    if new_y > new_x:
        new_tmp = new_x
        new_x = new_y
        new_y = new_tmp
    if y_axes > x_axes:
        tmp_axes = x_axes
        x_axes = y_axes
        y_axes = tmp_axes
        
    return x_axes, y_axes, new_x, new_y