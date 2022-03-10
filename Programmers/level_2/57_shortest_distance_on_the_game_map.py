def solution(maps):
    answer = 0
    return bfs(maps)

def bfs(maps):
    score_maps = init_score_maps(maps)
    score_maps[0][0] = 1
    queue = []
    find_next_route(0, 0, maps, queue, score_maps, 1)
    max_x, max_y = len(maps[0]) - 1, len(maps) - 1
    count = 2
    while queue:
        next_queue = []
        for x, y in queue:
            find_next_route(x, y, maps, next_queue, score_maps, count)
            if x == max_x and y == max_y:
                return count
        count += 1
        queue = next_queue
    return -1

def init_score_maps(maps):
    score_maps = []
    for y in range(len(maps)):
        score_col = [0 for _ in range(len(maps[y]))]
        score_maps.append(score_col)
    return score_maps
    
def find_next_route(x, y, maps, queue, score_maps, count):
    max_x, max_y = len(maps[0]) - 1, len(maps) - 1
    if x != 0 and score_maps[y][x - 1] == 0 and maps[y][x - 1] == 1:
        score_maps[y][x - 1] = count
        queue.append([x - 1, y])
    if y != 0 and score_maps[y - 1][x] == 0 and maps[y - 1][x] == 1:
        score_maps[y - 1][x] = count
        queue.append([x, y - 1])
    if x != max_x and score_maps[y][x + 1] == 0 and maps[y][x + 1] == 1:
        score_maps[y][x + 1] = count
        queue.append([x + 1, y])
    if y != max_y and score_maps[y + 1][x] == 0 and maps[y + 1][x] == 1:
        score_maps[y + 1][x] = count
        queue.append([x, y + 1])