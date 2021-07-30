def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(returnBitLower(number))
    return answer

def returnOneBitCount(number):
    bit = []
    while number > 1:
        if number % 2 != 0:
            bit.append(1)
        else:
            bit.append(0)
        number //= 2
        
    if number == 1:
        bit.append(1)
        
    return bit
    
def returnBitLower(number):
    if number % 2 == 0:
        return number + 1
    else:
        originBit = returnOneBitCount(number)
        if originBit.count(1) == len(originBit):
            originBit[len(originBit) - 1] = 0
            originBit.append(1)
        else:
            cacheIndex = 0
            for i in range(len(originBit)):
                if originBit[i] == 0:
                    originBit[i] = 1
                    cacheIndex = i
                    break
                    
            for i in range(cacheIndex - 1, -1, -1):
                if originBit[i] == 1:
                    originBit[i] = 0
                    break     
            
        return bitToNumber(originBit)
    
def bitToNumber(originBit):
    answer = 0
    for i in range(len(originBit)):
        if i == 0 and originBit[i] == 1:
            answer += 1
        elif originBit[i] == 1:
            answer += (2 ** i)
            
    return answer