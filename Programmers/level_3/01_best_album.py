def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic.keys():
            dic[genres[i]] = []
            dic[genres[i]].append(plays[i])
            dic[genres[i]].append([plays[i],i])
        else:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]].append([plays[i],i])
    a = sorted(dic.items(), reverse=True, key=lambda t : t[1][0])
    for key in a:
        count = 0
        for val in sorted(key[1][1:],key = lambda x : (-x[0], x[1])):
            count += 1
            answer.append(val[1])
            if count == 2: break
    return answer