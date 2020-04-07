def solution(citations):
    answer = 0
    HcountList = []
    citations.sort(reverse = True)
    print(citations)
    for index1 in range(len(citations)):
        Hcount = 0
        for index2 in range(len(citations)):
            if citations[index2] >= citations[index1]:
                Hcount += 1
        if Hcount >= citations[index1]:
             HcountList.append(citations[index1])
        else:
            HcountList.append(Hcount)
    HcountList.sort(reverse = True)
    return HcountList[0]