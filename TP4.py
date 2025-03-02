# Constructed Weighted graph by adjacent matrix
# Implemented Prim and Kruskal Algo obey behavior:
#   - Input: Ask user Root node
#   - Output: List of edges of Minimal Spanning Tree from 2 above algo as well as weighted sum of those tree

import heapq

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_vertices = len(matrix)

    # Implements Prim's Algorithm for MST
    def prim(self, start):

        visited = set()
        mst_edges = []
        min_heap = [(0, start, -1)]  # (weight, current_node, parent)
        total_weight = 0

        while len(visited) < self.num_vertices:
            weight, node, parent = heapq.heappop(min_heap)
            if node in visited:
                continue
            
            visited.add(node)
            if parent != -1:  # Ignore the starting node
                mst_edges.append((parent, node, weight))
                total_weight += weight

            # Push all adjacent nodes into the heap
            for neighbor, w in enumerate(self.matrix[node]):
                if w > 0 and neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, node))

        return mst_edges, total_weight

    # Implements Kruskal's Algorithm
    def kruskal(self):
        edges = []
        parent = list(range(self.num_vertices))
        rank = [0] * self.num_vertices

        # Extract edges from adjacency matrix
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):  # Avoid duplicate edges
                if self.matrix[u][v] > 0:
                    edges.append((self.matrix[u][v], u, v))

        # Sort edges by weight
        edges.sort()

        # Find function for Disjoint Set
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        # Union function for Disjoint Set
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
                return True
            return False

        mst_edges = []
        total_weight = 0

        # Apply Kruskal's Algorithm
        for weight, u, v in edges:
            if union(u, v):  # Only add edge if it connects different components
                mst_edges.append((u, v, weight))
                total_weight += weight

        return mst_edges, total_weight


if __name__ == "__main__":
    G = [
        [0, 4, 0, 0, 1, 0, 2, 0, 0],  # 1
        [4, 0, 7, 0, 0, 5, 0, 0, 0],  # 2
        [0, 7, 0, 1, 0, 8, 0, 0, 0],  # 3
        [0, 0, 1, 0, 0, 6, 4, 3, 0],  # 4
        [1, 0, 0, 0, 0, 9, 10, 0, 1],  # 5
        [0, 5, 8, 6, 9, 0, 0, 0, 2],  # 6
        [2, 0, 0, 4, 10, 0, 2, 0, 8],  # 7
        [0, 0, 0, 3, 0, 0, 0, 0, 1],  # 8
        [0, 0, 0, 0, 0, 2, 8, 1, 0],  # 9
    ]

    graph = Graph(G)

    # Input the starting node (converted to 0-based index)
    root = int(input("Enter root node (1-9): ")) - 1

    print("\n--- Prim's Algorithm ---")
    prim_mst, prim_weight = graph.prim(root)
    print("Edges in MST:", prim_mst)
    print("Total MST Weight:", prim_weight)

    print("\n--- Kruskal's Algorithm ---")
    kruskal_mst, kruskal_weight = graph.kruskal()
    print("Edges in MST:", kruskal_mst)
    print("Total MST Weight:", kruskal_weight)
