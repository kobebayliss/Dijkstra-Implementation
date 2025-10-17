import heapq
import sys

def dijkstra(graph, n, source):
    """
    Compute shortest paths from source to all nodes using Dijkstra's algorithm.
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        n: Number of nodes
        source: Source node index
    
    Returns:
        List of shortest distances from source to each node
    """

    distance = [float('inf')]*n
    distance[source] = 0

    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        # Skip if already visited
        if u in visited:
            continue

        visited.add(u)

        # Skip if outdated
        if current_distance > distance[u]:
            continue
        
        # Relax edges
        if u in graph:
            for v, weight in graph[u]:
                new_distance = distance[u] + weight

                # Found new shortest path
                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(priority_queue, (new_distance, v))

    return distance


lines = sys.stdin.read().strip().split("\n")
parts = lines[0].split()
n = int(parts[0])
m = int(parts[1])

graph = {}
for i in range(1, m + 1):
    data = lines[i].split()
    u, v, t = int(data[0]), int(data[1]), int(data[2])
    if u not in graph:
        graph[u] = []
    graph[u].append((v, t))

source = int(lines[m + 1])

distances = dijkstra(graph, n, source)
for k in range(n):
    print(f"Sector {k}: Travel time = {distances[k]}")