# An example of algorithm for detecting path existence.
# Path_Existence(G, s, t)
# 1. Mark as visited (u = s)
# 2. Repeat until no more vertices can be marked:
#   + Iterate through all edges. If an edge (u, v) is found, such that u is marked and v is not, 
#   then mark v as visited.
# 3. If t is marked visited than report yes and stop. Otherwise. report no and stop

# Req: Input Path_Existence and test check for the graph in Pref Prog Lang following behaviour:
#  1. Ask user input 2 nodes
#  2. Return True if path exist else False
# Submit format: TP1.<Ex1>

# Let G be an undirected graph. Prove that the sum of the degrees of vertices of G is always an even number
#   + Using the matrix representation, find all the connected component of each graph
#   + Prove that the number of vertices of odd degree in any graph G is even
#   + To implement the PathExistence(G, s, v) algo
#   + To implement an algo tha given (G, s, t) return the squence of vertices that composes the path
#   + Given a graph and a path, to develop an algo for checking if the path is unique

from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u) 

    def path_existence(self, start, target):
        if start not in self.adjacency_list or target not in self.adjacency_list:
            return False

        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            current = queue.popleft()
            if current == target:
                return True
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

graph = Graph()
graph.add_edge(1, 2)

graph.add_edge(2, 1)
graph.add_edge(2, 5)

graph.add_edge(3, 6)

graph.add_edge(4, 6)
graph.add_edge(4, 7)

graph.add_edge(5, 2)

graph.add_edge(6, 3)
graph.add_edge(6, 4)
graph.add_edge(6, 7)

graph.add_edge(7, 4)
graph.add_edge(7, 6)

# User input
start = int(input("Enter start node: "))
target = int(input("Enter target node: "))

if graph.path_existence(start, target):
    print("Path exists.")
else:
    print("No path exists.")
