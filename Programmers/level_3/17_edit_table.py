def solution(n, k, cmd):
    linked_list = get_linked_list(n)
    stack = []
    pos = k
    for cmd_str in cmd:
        command, param = get_cmd_and_param(cmd_str)
        if command == "U":
            pos = read_up(pos, int(param), linked_list)
        elif command == "D":
            pos = read_down(pos, int(param), linked_list)
        elif command == "Z":
            reset_index = stack.pop()
            reset(reset_index, linked_list)
        elif command == "C":
            stack.append(pos)
            pos = delete(pos, linked_list)
    return get_answer(n, stack)

def get_answer(n, stack):
    answer = ["O"] * n
    for i in stack:
        answer[i] = "X"
    return "".join(answer)

def get_cmd_and_param(cmd_str):
    cmd = ""
    param = ""
    split_cmd = cmd_str.split(" ")
    cmd = split_cmd[0]
    if len(split_cmd) == 2:
        param = split_cmd[1]
    return cmd, param
    
def get_linked_list(n):
    linked_list = []
    for i in range(n):
        start = i - 1
        end = i + 1
        linked_list.append([start, end])
    linked_list[0][0] = n - 1
    linked_list[-1][1] = 0
    return linked_list

def reset(reset_index, linked_list):
    before = linked_list[reset_index][0]
    after = linked_list[reset_index][1]
    linked_list[before][1] = reset_index
    linked_list[after][0] = reset_index

def delete(pos, linked_list):
    before = linked_list[pos][0]
    after = linked_list[pos][1]
    linked_list[before][1] = after
    linked_list[after][0] = before
    if after == 0:
        return before
    return after
    
def read_down(pos, move, linked_list):
    for i in range(move):
        next_i = linked_list[pos][1]
        pos = next_i
    return pos

def read_up(pos, move, linked_list):
    for i in range(move):
        next_i = linked_list[pos][0]
        pos = next_i
    return pos