def solution(n, lost, reserve):
    studentField = []
    answer = 0
    for i in range(n):
        studentField.append(0)
    for res in reserve:
        studentField[res-1] += 1
    for ls in lost:
        studentField[ls-1] -= 1
    for i in range(n):
        print(studentField, answer)
        if studentField[i] != 1:
            continue
        if i == 0:
            if studentField[i+1] == -1:
                #answer += 1
                studentField[i+1] = 0
                studentField[i] = 0
        elif i >= n-1:
            if studentField[i-1] == -1:
                #answer += 1
                studentField[i-1] = 0
                studentField[i] = 0
        else:
            if studentField[i-1] == -1:
                #answer += 1
                studentField[i-1] = 0
                studentField[i] = 0
            elif studentField[i+1] == -1:
                #answer += 1
                studentField[i+1] = 0
                studentField[i] = 0
    for i in range(n):
        if studentField[i] >= 0:
            answer+=1
    return answer