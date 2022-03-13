import itertools
import copy

def solution(expression):
    answer = 0
    parse_exp, formula = parse(expression)
    priority = make_priority(formula)
    result = get_result(priority, parse_exp)
    return result

def get_result(priority, parse_exp):
    max_val = 0
    for pr_set in priority:
        next_exp_list = copy.deepcopy(parse_exp)
        for f in pr_set:
            next_list = []
            while len(next_exp_list) >= 3:
                a = next_exp_list[0]
                formula = next_exp_list[1]
                b = next_exp_list[2]
                
                if formula == f:
                    c = calculate(int(a), int(b), formula)
                    recursive_pop(3, next_exp_list)
                    next_exp_list.insert(0, c)
                    continue
                    
                next_list.append(a)
                next_list.append(formula)
                recursive_pop(2, next_exp_list)
            next_list += next_exp_list
            next_exp_list = next_list
        final_num = int(next_exp_list[0])
        if final_num > max_val: 
            max_val = final_num
        if (- final_num) > max_val:
            max_val = (- final_num)
    return max_val

def recursive_pop(count, next_exp_list):
    for _ in range(count):
        next_exp_list.pop(0)

def calculate(a, b, formula):
    if formula == "+":
        return str(a + b)
    if formula == "-":
        return str(a - b)
    if formula == "*":
        return str(a * b)
            
def make_priority(formula):
    formula_list = list(formula)
    return list(itertools.permutations(formula_list, len(formula_list)))

def parse(expression):
    parse_exp = []
    cache_str = ""
    formula = set()
    for exp_str in expression:
        if exp_str == "+":
            parse_exp.append(cache_str)
            parse_exp.append("+")
            formula.add("+")
            cache_str = ""
            continue
        if exp_str == "-":
            parse_exp.append(cache_str)
            parse_exp.append("-")
            formula.add("-")
            cache_str = ""
            continue
        if exp_str == "*":
            parse_exp.append(cache_str)
            parse_exp.append("*")
            formula.add("*")
            cache_str = ""
            continue
        cache_str += exp_str
    parse_exp.append(cache_str)
    return parse_exp, formula
    