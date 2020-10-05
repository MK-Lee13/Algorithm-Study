def solution(n, words):
    answer = [0, 0]
    position = 0
    character = 1
    beforeWord = ''
    cache = {}
    for word in words:
        if word in cache:
            return makeAnswer(character, position, n)
        
        if beforeWord != word[0] and beforeWord != '':
            return makeAnswer(character, position, n)
        cache[word] = 1 
        beforeWord = word[-1]
        character += 1
        position += 1
    return answer

def makeAnswer(character, position, n):
    character = character % n
    position = position // n
    if character == 0:
        return [n, position + 1]
    else:
        return [character, position + 1]