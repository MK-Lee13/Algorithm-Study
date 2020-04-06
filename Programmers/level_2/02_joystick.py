def solution(name):
    answer = 0
    Alength = 0
    Apart = 0
    Alist = []
    for index, spell in enumerate(name):
        upCase = ord(spell) - ord("A")
        downCase = ord("Z") - ord(spell) + 1
        if spell == "A":
            if Alength == 0:
                Apart = index
                Alength = 1
            elif Apart == (index - Alength):
                Alength += 1
        elif upCase > downCase:
            answer += downCase
            if Alength != 0:
                Alist.append([Alength, Apart])
                Apart = 0
                Alength = 0
        else:
            answer += upCase
            if Alength != 0:
                Alist.append([Alength, Apart])
                Apart = 0
                Alength = 0
    if Alength != 0:
        Alist.append([Alength, Apart])
        Apart = 0
        Alength = 0
    if len(Alist) != 0:
        print(Alist)
        Alist.sort(reverse=True)
        part = 100
        for Asort in Alist:
            if Asort[1] == 0:
                imm = 1
            else:
                imm = Asort[1]
            if len(name) == (Asort[0] + Asort[1]):
                tmpPart = (imm - 1)
            else:
                tmpPart = ((imm - 1) * 2) + (len(name) - Asort[1] - Asort[0])
            if tmpPart < part:
                part = tmpPart
        if part < (len(name) - 1):
            answer += part
        else:
            answer += (len(name) - 1)
    else:
        answer += (len(name) - 1)
    return answer