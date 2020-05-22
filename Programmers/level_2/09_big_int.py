def solution(numbers):
    answer = ''
    if (sum(numbers) == 0):
        return "0"
    sortNumber = refactor(numbers)
    sortNumber.sort(reverse = True)
    for sort in sortNumber:
        answer += str(numbers[sort[-1]]) 
    return answer

def refactor(numbers):
    sortNumber = []
    for index, number in enumerate(numbers):
        if number < 10:
            sortNumber.append((number *1000 + number * 100 + number*10 + number,3, index))
        elif number < 100:
            sortNumber.append((int(number/10) * 1000 + (number%10) * 100 + int(number/10) * 10 + number%10, 2 , index))
        elif number < 1000:
            sortNumber.append((int(number/100) * 1000 + (int(number/10)%10) * 100 + (number%10) * 10 + (number%10), 1, index))
        else:
            sortNumber.append((1000,0,index))
    return sortNumber