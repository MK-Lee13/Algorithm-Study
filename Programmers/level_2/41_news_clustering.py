def solution(str1, str2):
    low_str_1 = str1.lower()
    low_str_2 = str2.lower()
    str1_list = [w for w in low_str_1]
    str2_list = [w for w in low_str_2]
    str1_list = make_multiple_union(str1_list)
    str2_list = make_multiple_union(str2_list)
    
    same_list = same(str1_list, str2_list)
    union_list = union(str1_list, str2_list, same_list)
    
    if len(same_list) == len(union_list):
        return 65536
    if len(same_list) == 0 or len(union_list) == 0:
        return 0
    answer = (len(same_list) / len(union_list)) * 65536
    return int(answer)

def make_multiple_union(str_list):
    result = []
    for i in range(len(str_list) - 1):
        if str_list[i].isalpha() and str_list[i + 1].isalpha():
            result.append(str_list[i] + str_list[i + 1])
    return result    

def same(str1_list, str2_list):
    same = []
    copy1_list = [w for w in str1_list]
    copy2_list = [w for w in str2_list]
    while(len(copy1_list)):
        comp = copy1_list.pop(0)
        if comp in copy2_list:
            same.append(comp)
            copy2_list.remove(comp)
    return same
    
def union(str1_list, str2_list, same_list):
    union = []
    copy1_list = [w for w in same_list]
    copy2_list = [w for w in same_list]
    
    while(len(copy1_list)):
        comp = copy1_list.pop(0)
        if comp in str1_list:
            str1_list.remove(comp)
    union += str1_list
    
    while(len(copy2_list)):
        comp = copy2_list.pop(0)
        if comp in str2_list:
            str2_list.remove(comp)
    union += str2_list
    union += same_list
    return union