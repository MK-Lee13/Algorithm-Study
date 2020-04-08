def solution(priorities, location):
    answer =0
    sortPriorities = copyList(priorities)
    sortPriorities.sort(reverse = True)
    print(priorities, sortPriorities)
    while True:
        print(location, "L")
        print(answer,"A")
        print(priorities)
        if priorities[0] >= sortPriorities[0]:
            answer += 1
            if location == 0:
                return answer
            else:
                sortPriorities.pop(0)
                priorities.pop(0)
                location -= 1
        elif priorities[0] < sortPriorities[0]:
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            backNum = priorities.pop(0)
            priorities.append(backNum)
    return answer

def copyList(priorities):
    List = []
    for priority in priorities:
        List.append(priority)
    return List