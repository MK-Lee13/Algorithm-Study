def solution(phone_book):
    answer = True
    for index1 in range(len(phone_book)):
        for index2 in range(len(phone_book)):
            if index1 == index2:
                continue
            if phone_book[index2].find(phone_book[index1]) == 0:
                return False
    return answer