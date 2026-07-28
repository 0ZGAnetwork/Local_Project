def dfs(adj_matrix, node_no):
    n = len(adj_matrix)

    if not (0 <= node_no < n):
        raise ValueError(f"{node_no} must be a number between 0 and {n-1}")

    visited = [False] * n
    result = []
    
    def visit(v):
        visited[v] = True
        result.append(v)
        
        for u in range(n):
            if adj_matrix[v][u] == 1 and not visited[u]:
                visit(u)


    visit(node_no)
    return result
    # return visited


graph = [
    [0,1,1,1,0],  # 0 -> 1,2,3
    [1,0,0,0,0],  # 1 -> 0
    [1,0,0,0,1],  # 2 -> 0,4
    [1,0,0,0,0],  # 3 -> 0
    [0,0,1,0,0]   # 4 -> 2
]
print(dfs(graph, 0))

