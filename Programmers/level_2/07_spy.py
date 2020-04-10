def solution(clothes):
    answer = 1
    hashTable = {}
    for cloth in clothes:
        if cloth[1] in hashTable:
            hashTable[cloth[1]] += 1
        else:
            hashTable[cloth[1]] = 1
            
    for r in hashTable.values():
        answer *= (r+1)
    return answer - 1