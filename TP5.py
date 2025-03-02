# a) Present graph G using adjacent matrix
# b) Implement Dijkstra algo that obey behavior:
#   + Ask input Source (S) and Target (T)
#   + Return shortest path to move from (S) to (T) in (G)
#   + Return weighted sum of shortest path above
import heapq

class Graph:
    def __init__(self, matrix, labels):
        self.matrix = matrix
        self.num_vertices = len(matrix)
        self.labels = labels  # Node names (A, B, C, ...)

    # Implements Dijkstra's Algorithm to find the shortest path
    def dijkstra(self, start, target):
        start_index = self.labels.index(start)
        target_index = self.labels.index(target)

        distances = [float('inf')] * self.num_vertices
        distances[start_index] = 0
        previous_nodes = [-1] * self.num_vertices

        min_heap = [(0, start_index)]  # (cost, node)

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_node == target_index:
                break  # Stop early if reach the target

            for neighbor, weight in enumerate(self.matrix[current_node]):
                if weight > 0:  # Valid edge
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous_nodes[neighbor] = current_node
                        heapq.heappush(min_heap, (new_distance, neighbor))

        # Reconstruct the shortest path
        path = []
        node = target_index
        while node != -1:
            path.append(self.labels[node])
            node = previous_nodes[node]
        path.reverse()

        return path, distances[target_index]
if __name__ == "__main__":
    G = [
        #A  B  C  D  E  F  G  H  L  M    
        [0, 4, 1, 0, 0, 0, 0, 0, 0, 0],  # A
        [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],  # B
        [1, 0, 0, 8, 0, 7, 0, 0, 0, 0],  # C
        [0, 0, 8, 0, 0, 0, 0, 5, 0, 0],  # D
        [0, 0, 0, 0, 0, 1, 0, 2, 2, 0],  # E
        [0, 3, 1, 0, 1, 0, 0, 1, 0, 0],  # F
        [0, 0, 0, 0, 0, 0, 0, 3, 4, 4],  # G
        [0, 0, 0, 5, 2, 1, 3, 0, 6, 7],  # H
        [0, 0, 0, 0, 0, 0, 4, 6, 0, 1],  # L
        [0, 0, 0, 0, 0, 0, 4, 7, 1, 0],  # M
    ]

    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']

    graph = Graph(G, labels)

    # Input source and target
    start = input("Enter Source Node (A-M): ").strip().upper()
    target = input("Enter Target Node (A-M): ").strip().upper()

    if start not in labels or target not in labels:
        print("Invalid input. Please enter a valid node label.")
    else:
        path, total_weight = graph.dijkstra(start, target)

        print(f"Shortest Path from {start} to {target}: {' -> '.join(path)}")
        print(f"Total Path Weight: {total_weight}")