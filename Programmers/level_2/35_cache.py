def solution(cacheSize, cities):
    answer = 0
    cacheBuffer = []
    for city in cities:
        isHeat = LRU(cacheBuffer, cacheSize, city)
        if isHeat == True:
            answer += 1
        else:
            answer += 5
            
    return answer

def LRU(cacheBuffer, cacheSize, city):
    isHeat = False
    refactCity = city.lower()
    
    if cacheSize == 0:
        return isHeat
    
    if refactCity in cacheBuffer:
        isHeat = True
    
    if isHeat == False:
        if len(cacheBuffer) == cacheSize:
            cacheBuffer.pop(0)
        cacheBuffer.append(refactCity)
    else:
        cacheBuffer.remove(refactCity)
        cacheBuffer.append(refactCity)
            
    return isHeat