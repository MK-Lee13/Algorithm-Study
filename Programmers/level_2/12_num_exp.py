def solution(n):
    answer = 0
    index = 1
    sumIndex = 0
    while index != n+1:
        for i in range(index, n+1):
            sumIndex += i
            if sumIndex == n:
                answer += 1
                break
            elif sumIndex > n:
                break
        index += 1
        sumIndex = 0
    return answer