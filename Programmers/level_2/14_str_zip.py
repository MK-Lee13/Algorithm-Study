def solution(s):
    answer = 0
    split = 1
    ansList =[]
    if len(s) == 1:
        return 1
    
    while split <= len(s) // 2:
        spDict = {}
        start = 0
        index = 0
        beforeData = ""
        while start != len(s):
            if split + start > len(s):
                spDict[index + 1] = [s[start: len(s)], 1]
                start = len(s)
            else:
                if s[start: start+split] == beforeData:
                    spDict[index][1] += 1
                else:
                    index += 1
                    spDict[index] = [s[start: start+split], 1]
                    
                beforeData = s[start: start+split]
                start += split
                
        split += 1
        ansList.append(sumStr(spDict))
    return min(ansList)

def sumStr(spDict):
    answer = 0
    for key in spDict.values():
        answer += len(key[0])
        if key[1] > 999:
            answer += 4
        elif key[1] > 99:
            answer += 3
        elif key[1] > 9:
            answer += 2
        elif key[1] > 1:
            answer += 1
        
    return answer