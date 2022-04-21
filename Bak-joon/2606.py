from collections import deque

def to_input():
  n = int(input())
  k = int(input())
  link_list = []
  for _ in range(k):
    link_list.append([ int(w) for w in input().split() ])
  return n, link_list


def solution(n, link_list):
  graph = make_graph(n, link_list)
  queue = deque()
  queue.append(1)
  duplicate_check_map = { 1 : 1 }
  while queue:
    next_node = queue.popleft()
    for node in graph[next_node]:
      if node not in duplicate_check_map:
        queue.append(node)
        duplicate_check_map[node] = 1
  return len(duplicate_check_map) - 1


def make_graph(n, link_list):
  graph = [list() for _ in range(n + 1)]
  for node in link_list:
    n1 = node[0]
    n2 = node[1]
    graph[n1].append(n2)
    graph[n2].append(n1)
  return graph
n, link_list = to_input()
print(solution(n, link_list))