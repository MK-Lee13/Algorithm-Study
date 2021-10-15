def solution(enroll, referral, seller, amount):
    answer = []
    moneys = [0] * (len(enroll) + 1)
    
    center_map = make_center_map(enroll, referral)
    center_tree = make_center_tree(center_map, referral)
    seller_list = make_seller_list(center_map, seller, amount)
    
    for sell in seller_list:
        who = sell[0]
        resend_money = sell[1] * 100
        check_who_is_my_master(moneys, who, center_tree, resend_money)
    if len(moneys) > 0:
        return moneys[: -1]
    return moneys

def check_who_is_my_master(moneys, who, center_tree, resend_money):
    if who == -1:
        moneys[who] = resend_money
        return
    if resend_money == 0:
        return 
    next_resend_money = resend_money // 10
    moneys[who] += resend_money - next_resend_money
    my_master = center_tree[who]
    check_who_is_my_master(moneys, my_master, center_tree, next_resend_money)    

def make_seller_list(center_map, seller, amount):
    seller_list = []
    for i in range(len(seller)):
        sell = center_map[seller[i]]
        seller_list.append([sell, amount[i]])
    return seller_list

def make_center_map(enroll, referral):
    center_map = {}
    for i in range(len(enroll)):
        center_map[enroll[i]] = i
    center_map["-"] = -1
    return center_map

def make_center_tree(center_map, referral):
    center_tree = []
    for i in range(len(referral)):
        master = center_map[referral[i]]
        center_tree.append(master)
    return center_tree