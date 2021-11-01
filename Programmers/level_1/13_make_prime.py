import math

def solution(nums):
    answer = 0
    for i1 in range(0, len(nums)):
        for i2 in range(i1 + 1, len(nums)):
            for i3 in range(i2 + 1, len(nums)):
                num = nums[i1] + nums[i2] + nums[i3]
                if isPrime(num) == True:
                    answer += 1
    return answer

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True