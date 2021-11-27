def solution(n):
    answer = 0
    num_list = []
    while n != 0:
        num = n % 10
        num_list.append(str(num))
        n //= 10
    num_list.sort(reverse=True)
    num_str = "".join(num_list)
    return int(num_str)