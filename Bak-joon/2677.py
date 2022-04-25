from collections import deque

def to_input():
  n = int(input())
  map = []
  for i in range(n):
    map.append([ int(w) for w in input() ])
  return n, map


def solution(n, map):
  find_nodes = {}
  answer = []
  for y in range(n):
    for x in range(n):
      key = get_key(y, x)
      if key not in find_nodes and map[y][x] == 1:
        result = bfs(map, find_nodes, y, x)
        answer.append(result)
  answer.sort()
  print(len(answer))
  for ans in answer:
    print(ans)

def bfs(map, find_nodes, y, x):
    queue = deque()
    queue.append([y, x])
    n = len(map)
    count = 0
    find_nodes[get_key(y, x)] = 1
    while queue:
        next_node = queue.popleft()
        next_y, next_x = next_node
        if next_x > 0 and get_key(next_y, next_x - 1) not in find_nodes and map[next_y][next_x - 1] == 1:
          find_nodes[get_key(next_y, next_x - 1)] = 1
          queue.append([next_y, next_x - 1])
        if next_y > 0 and get_key(next_y - 1, next_x) not in find_nodes and map[next_y - 1][next_x] == 1:
          find_nodes[get_key(next_y - 1, next_x)] = 1
          queue.append([next_y - 1, next_x])
        if next_x < n - 1 and get_key(next_y, next_x + 1) not in find_nodes and map[next_y][next_x + 1] == 1:
          find_nodes[get_key(next_y, next_x + 1)] = 1
          queue.append([next_y, next_x + 1])
        if next_y < n - 1 and get_key(next_y + 1, next_x) not in find_nodes and map[next_y + 1][next_x] == 1:
          find_nodes[get_key(next_y + 1, next_x)] = 1
          queue.append([next_y + 1, next_x])
        count += 1
    return count

def get_key(y, x):
  return f"{y}-{x}"

n, map = to_input()
solution(n, map)