def solution(price, money, count):
    answer = -1
    cost_money = 0
    
    for i in range(count):
        cost_money += (i + 1) * price
    
    answer = cost_money - money
    
    if answer < 0:
        return 0
    
    return answer