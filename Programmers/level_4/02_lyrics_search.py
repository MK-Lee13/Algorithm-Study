def solution(words, queries):
    answer = []
    word_trie, reverse_word_trie = get_word_lists(words)
    cache = {}
    for query in queries:
        if query in cache:
            answer.append(cache[query])
            continue
        q_len = len(query)
        q_count, q_pos, match_str = get_query_val(query)
        q_ans = 0
        if match_str == "":
            q_ans = get_match_count(words, q_len)
            answer.append(q_ans)
            cache[query] = q_ans
            continue
        if q_pos == True:
            q_ans = get_match_count(reverse_word_trie.starts_with(match_str[::-1]), q_len)
        else:
            q_ans = get_match_count(word_trie.starts_with(match_str), q_len)
        answer.append(q_ans)
        cache[query] = q_ans
    return answer

def get_word_lists(words):
    word_trie = Trie()
    reverse_word_trie = Trie()
    for word in words:
        word_trie.insert(word)
        reverse_word_trie.insert(word[::-1])
    return word_trie, reverse_word_trie

def get_match_count(match_list, q_len):
    result = 0
    if match_list == None or len(match_list) == 0:
        return result
    for match_str in match_list:
        if len(match_str) == q_len:
            result += 1
    return result

def get_query_val(query):
    q_count = 0
    match_str = ""
    q_pos = True # Left: True, Right: False
    for i in range(len(query)):
        _str = query[i]
        if _str == "?":
            q_count += 1
            if match_str != "":
                q_pos = False
        else:
            match_str += _str
    return q_count, q_pos, match_str

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def starts_with(self, prefix):
        current_node = self.head
        words = []
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        return words