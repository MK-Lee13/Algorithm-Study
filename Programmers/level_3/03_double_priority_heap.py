def solution(operations):
    answer = []
    for op in operations:
        data = op.split(" ", 1)
        if data[0] == 'I':
            answer.append(int(data[1]))
        else:
            if len(answer) == 0:
                continue
            if data[1] == '1':
                answer.pop(answer.index(maxNum(answer)))
            else:
                answer.pop(answer.index(minNum(answer)))
    if len(answer) == 0:
        return [0,0]
    else:
        return [maxNum(answer), minNum(answer)]

def maxNum(answer):
    maxList = sorted(answer, reverse=True)
    return maxList[0]

def minNum(answer):
    minList = sorted(answer)
    return minList[0]