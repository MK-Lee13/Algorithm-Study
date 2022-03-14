from collections import deque

def solution(N, road, K):
    graph = make_graph(road, N)
    graph_dup = make_zero_graph(N)
    result = bfs(graph, graph_dup, K)
    return len(result)

def bfs(graph, graph_dup, k):
    queue = deque()
    queue.append(1)
    find_node_map = {1 : 0}
    check_map = {}
    while queue:
        current_node = queue.popleft()
        for next_node in range(2, len(graph[0])):
            if graph[current_node][next_node] == 0:
                continue
            max_val = graph_dup[current_node] + graph[current_node][next_node]
            check_key = f"{current_node} {next_node}"
            if max_val <= k and check_key not in check_map:
                find_node_map[next_node] = max_val
                queue.append(next_node)
                check_map[check_key] = 1
            if graph_dup[next_node] == 0 or graph_dup[next_node] > max_val:
                graph_dup[next_node] = max_val
    return find_node_map

def make_zero_graph(n):
    return [0 for _ in range(n + 1)]
    
def make_graph(road, n):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for dat in road:
        n1 = dat[0]
        n2 = dat[1]
        val = dat[2]
        if graph[n1][n2] == 0:
            graph[n1][n2] = val
            graph[n2][n1] = val
            continue
        graph[n1][n2] = min(val, graph[n1][n2])
        graph[n2][n1] = min(val, graph[n2][n1])
    return graph