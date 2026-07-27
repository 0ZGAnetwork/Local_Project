from algorithms.Dijkstra import shortest_path

INF = float('inf')
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

start_node = 0
target_node = 5

distance , path = shortest_path(adj_matrix, start_node, target_node)
print(f"Distance from {start_node} to {target_node}: {distance}, Path: {path}")