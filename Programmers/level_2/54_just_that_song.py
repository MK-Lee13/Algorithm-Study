def solution(m, musicinfos):
    my_note_list = get_my_note_list(m)
    answer_list = []
    for music_info in musicinfos:
        split_music_info = music_info.split(",")
        time = get_time(split_music_info[0], split_music_info[1])
        name = split_music_info[2]
        full_note_list = get_full_note_list(split_music_info[3], time)
        
        if is_valid(my_note_list, full_note_list) == True:
            answer_list.append([time, name])
            
    sort_answer_list = sorted(answer_list, key = lambda x: -x[0])
    if len(sort_answer_list) == 0:
        return '(None)'
    return sort_answer_list[0][1]

def is_valid(my_note_list, full_note_list):
    full_len = len(full_note_list)
    my_len = len(my_note_list)
    
    for i in range(full_len - my_len + 1):
        result = True
        for j in range(my_len):
            if my_note_list[j] != full_note_list[i + j]:
                result = False
                break
        if result == True:
            return True
    
    return False

def get_time(start, end):
    split_start = start.split(":")
    split_end = end.split(":")
    start_hour, start_min = int(split_start[0]), int(split_start[1])
    end_hour, end_min = int(split_end[0]), int(split_end[1])
    return (end_hour - start_hour) * 60 + (end_min - start_min)

def get_my_note_list(notes):
    my_note_list = []
    for i in range(len(notes)):
        str_note = notes[i]
        if str_note == "#":
            continue
        if i + 1 < len(notes) and notes[i + 1] == "#":
            my_note_list.append(str_note + "#")
        else:
            my_note_list.append(str_note)
    return my_note_list

def get_full_note_list(notes, time):
    part_note_list = []
    full_note_list = []
    for i in range(len(notes)):
        str_note = notes[i]
        if str_note == "#":
            continue
        if i + 1 < len(notes) and notes[i + 1] == "#":
            part_note_list.append(str_note + "#")
        else:
            part_note_list.append(str_note)
    
    part_note_length = len(part_note_list)
    part_note_index = 0
    
    for i in range(time):
        note = part_note_list[part_note_index]
        full_note_list.append(note)
        part_note_index = (part_note_index + 1) % part_note_length
        
    return full_note_list