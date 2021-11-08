from collections import deque
# 백준 1260번 문제를 참고 하였습니다.

def dfs(graph, start_node, find_nodes):
  # 깊이 우선 탐색
  # 그래프에서 가장 최상위 노드부터 하위 노드까지 제일깊게 탐색하고, 다시 위로 올라와서 탐색하는 방식
  find_nodes.append(start_node) # 탐색한 노드 들
  for next_node in range(len(graph[start_node])):
    if graph[start_node][next_node] == 1 and next_node not in find_nodes:
      dfs(graph, next_node, find_nodes)

def bfs(graph, start_node):
  # 너비 우선 탐색
  # 그래프에서 가장 최상위 노투드 부터 다음 차수를 모두 탐색하고, 그 다음 차수를 모두 탐색하는 방식
  find_nodes = [start_node] # 탐색한 노드 들
  queue = deque()
  queue.append(start_node)
  while queue:
    current_node = queue.popleft()
    for next_node in range(len(graph[current_node])):
      if graph[current_node][next_node] == 1 and next_node not in find_nodes: # 탐색한 적 없고 노드 끼리 이어져 있는 경우
        find_nodes.append(next_node)
        queue.append(next_node)
  return find_nodes


def make_input(n, nodes):
  graph = [[0] * (n + 1) for _ in range(n + 1)]
  for node in nodes:
    n1 = node[0]
    n2 = node[1]
    graph[n1][n2] = 1
    graph[n2][n1] = 1
  return graph

# CASE 1
g1 = make_input(4, [[1, 2],[1, 3],[1, 4],[2, 4],[3, 4]])
dfs_find_node1 = []
print(bfs(g1, 1))
dfs(g1, 1, dfs_find_node1)
print(dfs_find_node1)

# CASE 2
g2 = make_input(5, [[5, 4],[5, 2],[1, 2],[3, 4],[3, 1]])
dfs_find_node2 = []
print(bfs(g2, 3))
dfs(g2, 3, dfs_find_node2)
print(dfs_find_node2)

# CASE 3
g3 = make_input(1000, [[999, 1000]])
dfs_find_node3 = []
print(bfs(g3, 1000))
dfs(g3, 1000, dfs_find_node3)
print(dfs_find_node3)