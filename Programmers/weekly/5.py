from itertools import product

def solution(word):
    answer = 0
    comb1 = list(product(["A", "E", "I", "O", "U"], repeat=5))
    comb2 = list(product(["A", "E", "I", "O", "U"], repeat=4))
    comb3 = list(product(["A", "E", "I", "O", "U"], repeat=3))
    comb4 = list(product(["A", "E", "I", "O", "U"], repeat=2))
    comb5 = list(product(["A", "E", "I", "O", "U"], repeat=1))
    comb = comb5 + comb4 + comb3 + comb2 + comb1
    comb.sort()
    for i in range(len(comb)):
        if word == "".join(comb[i]):
            answer = i + 1
            break
    return answer