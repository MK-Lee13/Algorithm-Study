def make_prime_list():
    result = [1] * 1000001
    result[0] = 0
    result[1] = 0
    
    for i in range(2, 1000001):
        if result[i] == 0:
            continue
        for j in range(i * i, 1000001, i):
            result[j] = 0
            
    return result
                

def solution(n):
    answer = 0
    prime_list = make_prime_list()
    for i in range(n + 1):
        if prime_list[i] == 1:
            answer += 1
    return answer