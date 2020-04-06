def solution(heights):
    answer = []
    for index, height in enumerate(heights):
        copyIndex = index 
        while copyIndex >= 0:
            if heights[copyIndex] > height:
                answer.append(copyIndex + 1)
                break
            elif heights[copyIndex] <= height and copyIndex == 0:
                answer.append(0)
            copyIndex -= 1
    return answer