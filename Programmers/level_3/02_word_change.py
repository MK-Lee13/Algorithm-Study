def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    while begin != target:
        if compare(target, begin):
            begin = target
            answer += 1
            break
        for word in words:
            if compare(word, begin):
                begin = word
                answer += 1
                words.pop(words.index(word))
                break
    return answer

def compare(word, target):
    answer = 0
    for i in range(len(target)):
        if word[i] == target[i]:
            answer += 1
    if answer == len(target) - 1:
        return True
    else:
        return False