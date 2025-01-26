# Implement both DFS and BFS using AI agent
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node] - visited)

    return order

def dfs(graph, start):
    stack = [start]
    visited = set()
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack.extend(graph[node] - visited)

    return order

def main():
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    start_node = 'A'
    print("BFS Order:", bfs(graph, start_node))
    print("DFS Order:", dfs(graph, start_node))

if __name__ == "__main__":
    main()