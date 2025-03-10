from collections import deque

def bidirectional_search(graph, start, goal):
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start}
    backward_visited = {goal}
    forward_parent = {}
    backward_parent = {}

    while forward_queue and backward_queue:
        # Forward Search
        current_f = forward_queue.popleft()
        for neighbor in graph.get(current_f, []):
            if neighbor in backward_visited:
                path = reconstruct_bidirectional_path(forward_parent, backward_parent, start, goal, current_f, neighbor)
                return path
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited.add(neighbor)
                forward_parent[neighbor] = current_f

        # Backward Search
        current_b = backward_queue.popleft()
        for neighbor in graph.get(current_b, []):
            if neighbor in forward_visited:
                path = reconstruct_bidirectional_path(forward_parent, backward_parent, start, goal, neighbor, current_b)
                return path
            if neighbor not in backward_visited:
               backward_queue.append(neighbor)
               backward_visited.add(neighbor)
               backward_parent[neighbor] = current_b
    return None  # No path found

def reconstruct_bidirectional_path(forward_parent, backward_parent, start, goal, intersection_f, intersection_b):
    path_forward = [intersection_f]
    while path_forward[-1] != start:
      path_forward.append(forward_parent[path_forward[-1]])

    path_backward = [intersection_b]
    while path_backward[-1] != goal:
      path_backward.append(backward_parent[path_backward[-1]])

    return path_forward[::-1] + path_backward[1:]


graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F'],
  'D': ['B'],
  'E': ['B', 'G'],
  'F': ['C'],
  'G': ['E', 'H'],
  'H': ['G']
 }
start_location = 'A'
arena_entrance = 'H'
shortest_path = bidirectional_search(graph, start_location, arena_entrance)
print("Shortest Path to Arena:", shortest_path)  # Output: Shortest Path to Arena: ['A', 'B', 'E', 'G', 'H']