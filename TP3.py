# G = 1 -> 2, 3; 3 -> 4 -> 8; 2 -> 6, 5; 5 -> 7
# a) Construct adjacent Matrix for graph G
# b) Write Inorder algo to exploit tree G which obey behavior:
#   - Input node label (x)
#   - Print out all node of subtree (x) in (Inorder)

# Converts adjacency matrix to adjacency list representation
def build_adjacency_list(matrix):
    n = len(matrix)
    adjacency_list = {i + 1: [] for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adjacency_list[i + 1].append(j + 1)

    return adjacency_list

# Inorder traversal of tree starting from inputed node
def inorder_traversal(tree, node):
    if node not in tree:
        return

    children = sorted(tree[node])  # Sort children for correct order

    if len(children) >= 1:
        inorder_traversal(tree, children[0])  # Left child
    
    print(node, end=" ")  # Print the current node

    if len(children) > 1:
        for i in range(1, len(children)):  # Right children
            inorder_traversal(tree, children[i])

if __name__ == "__main__":
    G = [
        [0, 1, 1, 0, 0, 0, 0, 0],  # 1 -> 2, 3
        [0, 0, 0, 0, 1, 1, 0, 0],  # 2 -> 5, 6
        [0, 0, 0, 1, 0, 0, 0, 0],  # 3 -> 4
        [0, 0, 0, 0, 0, 0, 0, 1],  # 4 -> 8
        [0, 0, 0, 0, 0, 0, 1, 0],  # 5 -> 7
        [0, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 0, 0, 0, 0, 0, 0],  # 7
        [0, 0, 0, 0, 0, 0, 0, 0],  # 8
    ]

    # Convert adjacency matrix to adjacency list
    tree = build_adjacency_list(G)

    # Input the starting node for inorder traversal
    root = int(input("Enter starting node: "))

    print("Inorder traversal of subtree rooted at node", root, ":")
    inorder_traversal(tree, root)
    print()
