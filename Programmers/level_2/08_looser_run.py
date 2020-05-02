def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for index in range(len(completion)):
        if participant[index] != completion[index]:
            return participant[index]
        
    return participant[-1]