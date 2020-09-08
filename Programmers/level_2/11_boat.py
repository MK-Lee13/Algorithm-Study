def solution(people, limit):
    people.sort()
    result = 0
    lIndex = 0
    hIndex = -1
    while lIndex - hIndex <= len(people) :
        result += 1
        if people[lIndex] + people[hIndex] <= limit:
            lIndex +=1
        hIndex -= 1
        
    return result