def solution(m, n, board):
    answer = 0
    board_list = make_board_list(board)
    isContinue = True
    while isContinue:
        remove_block = get_remove_block(m, n, board_list)
        if len(remove_block) == 0:
            break
        answer += len(remove_block)
        set_remove_block(remove_block, board_list)
        recover_block(m, n, board_list)
    return answer

def print_b(board):
    for br in board:
        print(br)

def make_board_list(board):
    board_list = []
    for br in board:
        board_list.append([i for i in br])
    return board_list

def isZero(data):
    if data == "0":
        return True
    return False

def validate(x1, x2, y1, y2):
    if isZero(x1) or isZero(x2) or isZero(y1) or isZero(y2):
        return False
    if x1 == x2 and y1 == y2 and x1 == y1:
        return True
    return False

def get_remove_block(m, n, board):
    remove_block = set()
    for i in range(m - 1):
        for j in range(n - 1):
            x1 = board[i][j]
            x2 = board[i][j + 1]
            y1 = board[i + 1][j]
            y2 = board[i + 1][j + 1]
            if validate(x1, x2, y1, y2):
                remove_block.add(f"{i},{j}")
                remove_block.add(f"{i + 1},{j}")
                remove_block.add(f"{i},{j + 1}")
                remove_block.add(f"{i + 1},{j + 1}")
    return remove_block

def set_remove_block(remove_block, board):
    for rm in remove_block:
        data = rm.split(",")
        board[int(data[0])][int(data[1])] = "0"
    return remove_block

def recover_block(m, n, board):
    for j in range(n - 1, -1, -1):
        for i in range(m - 1, -1, -1):
            if board[i][j] == "0":
                low_index = get_low_num(i, j, board)
                if low_index == -1:
                    break
                board[i][j] = board[low_index][j]
                board[low_index][j] = "0"
                
            
def get_low_num(i, j, board):
    for k in range(i - 1, -1, -1):
        if board[k][j] != "0":
            return k
    return -1