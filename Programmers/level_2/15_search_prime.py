from itertools import permutations
import math

def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        permuList = list(permutations(numbers, i))
        for permu in permuList:
            if isPrime(int(''.join(permu))):
                answer.append(int(''.join(permu)))
    return len(list(set(answer)))

def isPrime(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        if number == 2: 
            return True
        else:
            return False
    i = 3
    while  math.sqrt(number) >= i:
        if number % i == 0:
            return False
        i += 2
    return True