import sys
sys.setrecursionlimit(10**7)

def solution(tickets):
    start_icn = []
    aps = []
    tickets.sort()
    for ticket in tickets:
        if ticket[0] == "ICN":
            start_icn.append(ticket)
    total_result = []
    for start in start_icn:
        next_ap = start[1]
        copy_tickets = copy(tickets)
        copy_tickets.remove(start)
        dfs(copy_tickets, total_result, [start], next_ap)
    answers = finish_check(total_result)
    
    return answers[0]
    
def finish_check(total_result):
    answer = []
    for result in total_result:
        tmp = [result[0][0]]
        for airport in result:
            tmp.append(airport[1])
        answer.append(tmp)
    return answer

def copy(base):
    return [w for w in base]
    
def dfs(tickets, total_result, before_result, next_ap):
    if len(tickets) == 0:
        total_result.append(before_result)
        return
    
    for i in range(len(tickets)):
        ticket = tickets[i]
        if next_ap == ticket[0]:
            copy_tickets = copy(tickets)
            copy_tickets.pop(i)
            plust_result = before_result + [ticket]
            dfs(copy_tickets, total_result, plust_result, ticket[1])