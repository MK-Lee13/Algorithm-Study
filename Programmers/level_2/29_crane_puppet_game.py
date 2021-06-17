def solution(board, moves):
    answer = 0
    pang_pang = []
        
    for move in moves:
        index = move - 1
        
        last_pang = len(board[index])
        for i in range(last_pang):
            if board[i][index] != 0:
                pang_pang.append(board[i][index])
                board[i][index] = 0
                break
        
        answer += check_pang_pang(pang_pang)
    return answer

def check_pang_pang(pang_pang):
    if len(pang_pang) < 2:
        return 0
    if pang_pang[-1] == pang_pang[-2]:
        pang_pang.pop(-1)
        pang_pang.pop(-1)
        return 2
    return 0