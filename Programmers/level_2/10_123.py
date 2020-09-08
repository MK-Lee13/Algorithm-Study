def solution(n):
    defineList = [1,2,4]
    string = ""
    while n > 0:
        tmp = n % 3
        print(tmp)
        if tmp == 0:
            string = str(defineList[2]) + string
            n -= 1
        else:
            string = str(defineList[tmp-1]) + string
        n = n // 3
            
    return string