def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        is_min = return_cut_diff(wires, i)
        if is_min < answer:
            answer = is_min
    return answer

def return_cut_diff(wires, ignore_index):
    node = []
    edge = set()
    is_change = True
    if ignore_index == 0:
        edge.add(f"{wires[1][0]},{wires[1][1]}")
        node.append(wires[1][0])
        node.append(wires[1][1])
    else:
        edge.add(f"{wires[0][0]},{wires[0][1]}")
        node.append(wires[0][0])
        node.append(wires[0][1])
        
    while is_change:
        is_change = False
        for i in range(len(wires)):
            if i == ignore_index:
                continue
            if wires[i][0] in node and wires[i][1] in node:
                continue
            elif wires[i][0] in node:
                is_change = True
                edge.add(f"{wires[i][0]},{wires[i][1]}")
                node.append(wires[i][1])
            elif wires[i][1] in node:
                is_change = True
                edge.add(f"{wires[i][0]},{wires[i][1]}")
                node.append(wires[i][0])
                
    one_len = len(edge)
    two_len = len(wires) - one_len - 1
    
    if two_len > one_len:
        return two_len - one_len
    else:
        return one_len - two_len