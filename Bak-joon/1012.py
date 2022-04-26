from collections import deque

def to_input():
  t = int(input())
  for _ in range(t):
    m, n, k = [ int(w) for w in input().split() ]
    cabbage_list = []
    for _ in range(k):
      cabbage_list.append([ int(w) for w in input().split() ])
    c_map = make_map(m, n, cabbage_list)
    solution(m, n, c_map)

def make_map(m, n, cabbage_list):
  c_map = [[0] * m for _ in range(n)]
  for node in cabbage_list:
    x, y = node
    c_map[y][x] = 1
  return c_map

def solution(m, n, c_map):
  find_nodes = {}
  count = 0
  for y in range(n):
    for x in range(m):
      key = get_key(y, x)
      if key not in find_nodes and c_map[y][x] == 1:
        bfs(m, n, c_map, find_nodes, y, x)
        count += 1
  print(count)

def bfs(m, n, c_map, find_nodes, y, x):
    queue = deque()
    queue.append([y, x])
    find_nodes[get_key(y, x)] = 1
    while queue:
        next_node = queue.popleft()
        next_y, next_x = next_node
        if next_x > 0 and get_key(next_y, next_x - 1) not in find_nodes and c_map[next_y][next_x - 1] == 1:
          find_nodes[get_key(next_y, next_x - 1)] = 1
          queue.append([next_y, next_x - 1])
        if next_y > 0 and get_key(next_y - 1, next_x) not in find_nodes and c_map[next_y - 1][next_x] == 1:
          find_nodes[get_key(next_y - 1, next_x)] = 1
          queue.append([next_y - 1, next_x])
        if next_x < m - 1 and get_key(next_y, next_x + 1) not in find_nodes and c_map[next_y][next_x + 1] == 1:
          find_nodes[get_key(next_y, next_x + 1)] = 1
          queue.append([next_y, next_x + 1])
        if next_y < n - 1 and get_key(next_y + 1, next_x) not in find_nodes and c_map[next_y + 1][next_x] == 1:
          find_nodes[get_key(next_y + 1, next_x)] = 1
          queue.append([next_y + 1, next_x])

def get_key(y, x):
  return f"{y}-{x}"

to_input()