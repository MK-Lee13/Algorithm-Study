from itertools import combinations

def solution(numbers, target):
    answer = 0
    targetList = [i for i in range(len(numbers))]
    for i in range(len(numbers)):
        tpList = list(combinations(targetList, i))
        for tp in tpList:
            if (sumT(numbers, tp) == target):
                answer += 1
        
    return answer

def sumT(numbers, tp):
    sumNum = 0
    for j in tp:
        sumNum -= numbers[j]
        
    for i in range(len(numbers)):
        if i not in tp:
            sumNum += numbers[i]
            
    return sumNum
        