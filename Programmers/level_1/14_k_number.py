def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        split_array = array[i - 1: j]
        split_array.sort()
        answer.append(split_array[k - 1])
    return answer