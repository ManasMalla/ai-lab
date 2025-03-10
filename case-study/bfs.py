from collections import deque

def bfs(graph, start, targets):
    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        current = queue.popleft()

        if current in targets:
            path = reconstruct_path(parent, start, current)
            return path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return None  # or [] or "No Pokemon Found"

def reconstruct_path(parent, start, target):
    path = [target]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return path[::-1]

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C', 'H'],
    'G': ['E'],
    'H': ['F']
}
start_node = 'A'
target_nodes = ['G', 'H']
shortest_path = bfs(graph, start_node, target_nodes)
print("Shortest Path:", shortest_path) # Output: Shortest Path: ['A', 'B', 'E', 'G']