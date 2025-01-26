# Write a program to implement and solve water jug problem
# I.S: Two water jugs are empty
# Take capacity of 3L and 5L
# Goal State: One jug contains 4L of water

from collections import deque

def is_goal_state(state):
    return state[0] == 4 or state[1] == 4

def get_successors(state, capacities):
    successors = []
    jug1, jug2 = state
    cap1, cap2 = capacities

    # Fill Jug1
    successors.append((cap1, jug2))
    # Fill Jug2
    successors.append((jug1, cap2))
    # Empty Jug1
    successors.append((0, jug2))
    # Empty Jug2
    successors.append((jug1, 0))
    # Pour Jug1 to Jug2
    pour_to_jug2 = min(jug1, cap2 - jug2)
    successors.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
    # Pour Jug2 to Jug1
    pour_to_jug1 = min(jug2, cap1 - jug1)
    successors.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    return successors

def bfs(initial_state, capacities):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        (current_state, path) = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)
        path = path + [current_state]

        if is_goal_state(current_state):
            return path

        for successor in get_successors(current_state, capacities):
            if successor not in visited:
                queue.append((successor, path))

    return None

def main():
    initial_state = (0, 0)
    capacities = (3, 5)
    solution = bfs(initial_state, capacities)

    if solution:
        print("Solution found:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

