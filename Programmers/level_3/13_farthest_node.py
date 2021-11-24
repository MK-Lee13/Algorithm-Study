from collections import deque

def solution(n, edge):
    result = []
    g = make_graph(n, edge)
    count = bfs(g, 1)
    return count.count(max(count))

def make_graph(n, nodes):
    graph = [list() for _ in range(n + 1)]
    for node in nodes:
        n1 = node[0]
        n2 = node[1]
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph

def bfs(graph, start_node):
    find_nodes = {start_node : 1}
    queue = deque()
    queue.append([start_node, 1])
    count = []
    while queue:
        current_data = queue.popleft()
        current_node = current_data[0]
        current_depth = current_data[1]
        count.append(current_depth)
        for next_node in graph[current_node]:
            if next_node not in find_nodes:
                find_nodes[next_node] = 1
                queue.append([next_node, current_depth + 1])
    return count