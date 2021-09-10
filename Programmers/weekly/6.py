def solution(weights, head2head):
    answer = []
    members_key = make_key(weights)
    for i in range(len(head2head)):
        me = weights[i] # 나의 몸무게
        for j in range(len(head2head[0])):
            you = weights[j] # 상대 선수의 몸무게
            if head2head[i][j] == "N":
                continue
            members_key[i][0] += 1
            
            if head2head[i][j] == "W":
                members_key[i][1] += 1
                if me < you:
                    members_key[i][3] += 1
            if members_key[i][1] == 0:
                continue
                
            members_key[i][2] = members_key[i][1] / members_key[i][0]
    answer = sorted(members_key, key = lambda x : (-x[2], -x[3], -x[4], x[5]))
    return return_answer(answer)

def return_answer(answer):
    real_answer = []
    for key in answer:
        real_answer.append(key[5])
    return real_answer

def make_key(weights):
    members_key = []
    for i in range(len(weights)):
        member_key = []
        member_key.append(0) #[0] 총 뜬 횟수
        member_key.append(0) # [1] 내가 이긴횟수
        member_key.append(0) # [2] 승률
        member_key.append(0) # [3] 내 몸무게 보다 높은 선수 이긴 횟수
        member_key.append(weights[i]) # [4] 자신의 몸무게
        member_key.append(i + 1) # [5] 자신의 인덱스
        members_key.append(member_key)
    return members_key