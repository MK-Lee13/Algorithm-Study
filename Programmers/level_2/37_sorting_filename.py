def solution(files):
    answer = []
    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    not_sort_list = []
    for file in files:
        head_str, number_str, tail_str = get_head_number_tail(file, num_list)
        not_sort_list.append([
            head_str,
            int(number_str),
            tail_str,
            file
        ])
    sort_list = sorted(not_sort_list, key = lambda x : (x[0], x[1]))
    return [sort[3] for sort in sort_list]

def get_head_number_tail(file, num_list):
    get_head = False
    is_end = False
    number_str = ""
    head_str = ""
    tail_str = ""
    for char in file:
        if char in num_list and is_end == False:
            get_head = True
            number_str += char
        elif get_head == False:
            head_str += char
        else:
            is_end = True
            tail_str += char
    return head_str.lower(), number_str, tail_str.lower()