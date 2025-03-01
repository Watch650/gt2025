# Let G be an undirected graph. Prove that the sum of the degrees of vertices of G is always an even number
#   + Using the matrix representation, find all the connected component of each graph
#   + Prove that the number of vertices of odd degree in any graph G is even
#   + To implement the PathExistence(G, s, v) algo
#   + To implement an algo tha given (G, s, t) return the squence of vertices that composes the path
#   + Given a graph and a path, to develop an algo for checking if the path is unique

# Find components of a graph which is represented by Adjacency matrix
# Behavior:
#   + Input: Graph represented by matrix
#   + Output: Number of components both weak and strong

# + Give the directed graph as a matrix represent
# + Return number of weakly connected component (optional: and strongly connected component) 

def dfs(graph, node, visited, stack=None):
    visited[node] = True
    for neighbor in range(len(graph)):
        if graph[node][neighbor] and not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    if stack is not None:
        stack.append(node)

# Transposes the given adjacency matrix (reverse edges)
def transpose_graph(graph):
    n = len(graph)
    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][i] = graph[i][j]
    return transposed

# Kosaraju's Algorithm for finding SCCs
def kosaraju_scc(graph):
    n = len(graph)
    visited = [False] * n
    stack = []

    # Perform DFS and fill stack
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    transposed_graph = transpose_graph(graph)

    # Process nodes in order of decreasing finish time
    visited = [False] * n
    scc_count = 0

    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs(transposed_graph, node, visited)
            scc_count += 1  # Each DFS marks a new SCC

    return scc_count

# Counts the number of weakly connected components
def weakly_connected_components(graph):
    n = len(graph)

    # Convert directed graph to undirected graph
    undirected = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] or graph[j][i]:  # If there is a connection in either direction
                undirected[i][j] = 1
                undirected[j][i] = 1

    # Find connected components using DFS
    visited = [False] * n
    wcc_count = 0

    for i in range(n):
        if not visited[i]:
            dfs(undirected, i, visited)
            wcc_count += 1  # Each DFS marks a new component

    return wcc_count

if __name__ == "__main__":
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 0, 0, 1, 0, 0, 0],  # 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 0, 1, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 1, 0, 1, 0, 0, 1, 0],  # 7
        [0, 0, 1, 0, 0, 0, 0, 0, 1],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
    ]

    print("Adjacency Matrix:")
    for row in G:
        print('  '.join(map(str, row)))

    num_wcc = weakly_connected_components(G)
    num_scc = kosaraju_scc(G)

    print(f"\nWeakly Connected Components: {num_wcc}")
    print(f"Strongly Connected Components: {num_scc}")

