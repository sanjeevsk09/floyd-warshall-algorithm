INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF for _ in range(n)] for _ in range(n)]

    # Initialize the distance matrix with direct edge weights
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif (i, j) in graph:
                dist[i][j] = graph[(i, j)]

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
# Create a graph represented as a dictionary where keys are (from, to) pairs and values are edge weights.
graph = {
    (0, 1): 3,
    (0, 2): 6,
    (1, 2): 2,
    (1, 3): 1,
    (2, 1): 4,
    (2, 3): 2,
    (3, 0): 3,
    (3, 2): 7
}

result = floyd_warshall(graph)

# Display the shortest path matrix
for row in result:
    print(row)
