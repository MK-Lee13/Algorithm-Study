import sys
sys.setrecursionlimit(10000000)

def solution(k, room_number):
    answer = []
    rooms = {}
    for room in room_number:
        answer.append(get_room(room, rooms))    
    return answer

def get_room(room, rooms):
    if room not in rooms:
        rooms[room] = room + 1
        return room
    
    key = rooms[room]
    value = get_room(key, rooms)
    rooms[room] = value + 1
    return value
    