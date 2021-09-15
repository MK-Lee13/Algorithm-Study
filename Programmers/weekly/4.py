def solution(table, languages, preference):
    answer = ''
    preference_table = make_preference_table(table)
    answer_list = calculate_langs(preference_table, languages, preference)
    sorted_answer = sorted(answer_list, key = lambda x : (-x[0], x[1]))
    return sorted_answer[0][1]

def calculate_langs(preference_table, languages, preference):
    result = []
    for key in preference_table:
        value = 0
        for i in range(len(languages)):
            language = languages[i]
            if language in preference_table[key]:
                value += preference_table[key][language] * preference[i]
        result.append([value, key])
    return result
            

def make_preference_table(table):
    result = {}
    for cell in table:
        cell_list = cell.split()
        result[cell_list[0]] = {}
        for i in range(1, 6):
            result[cell_list[0]][cell_list[i]] = 6 - i
    return result