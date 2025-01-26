import copy
from collections import deque
import random

game = []
game_state = [1,2,3,4,5,6,7,8,-1]
random.shuffle(game_state)

for i in range(3):
    game.append([])
    for j in range(3):
        game[i].append(game_state.pop())
print(game)

# BFS to solve the 8-puzzle problem
def bfs_8_puzzle(start, goal):
   
    def find_empty_tile(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == -1:
                    return i, j

    def get_neighbors(state):
        neighbors = []
        x, y = find_empty_tile(state)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy.deepcopy(state)
                # Swap empty tile with the adjacent tile
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)
        return neighbors

    def state_to_tuple(state):
        return tuple(tuple(row) for row in state)

    # BFS
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path + [current_state]

        visited.add(state_to_tuple(current_state))
        for neighbor in get_neighbors(current_state):
            if state_to_tuple(neighbor) not in visited:
                queue.append((neighbor, path + [current_state]))

    return None  # No solution found

# Goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]

solution = bfs_8_puzzle(game, goal_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")