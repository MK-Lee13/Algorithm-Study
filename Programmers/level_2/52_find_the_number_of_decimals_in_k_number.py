import math

def solution(n, k):
    answer = 0
    notation_str = get_k_notation(k, n)
    split_notation_str = get_split_notation_str(notation_str)
    
    for i in range(len(split_notation_str)):
        target = split_notation_str[i]
        if is_prime_number(int(target)) == True:
            answer += 1
    return answer

def get_split_notation_str(notation_str):
    split_notation_str = []
    cache_str = ""
    for n_str in notation_str:
        if n_str == "0":
            if cache_str != "":
                split_notation_str.append(cache_str)
                cache_str = ""
            split_notation_str.append(n_str)
        else:
            cache_str += n_str
    if cache_str != "":
        split_notation_str.append(cache_str)
    return split_notation_str

def is_prime_number(n):
	if n == 0 or n == 1:
		return False
	if n == 2:
		return True
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def get_k_notation(k, n):
    notation_str = ""
    while n > 0:
        notation_str += str(n % k)
        n = n // k
    return notation_str[::-1]