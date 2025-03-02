# a) Present graph G using adjacent matrix
# b) Implement Dijkstra algo that obey behavior:
#   + Ask input Source (S) and Target (T)
#   + Return shortest path to move from (S) to (T) in (G)
#   + Return weighted sum of shortest path above

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