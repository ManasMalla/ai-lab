import random
import math

class Obstacles:
    def __init__(self):
      self.blocked_paths = {} # (room1, room2, time) : True or False

    def is_path_blocked(self, room1, room2, time):
        if (room1, room2, time) in self.blocked_paths:
            return self.blocked_paths[(room1, room2, time)]
        return False # No path was blocked

    def set_block_time(self, room1, room2, start_time, end_time):
        """ Set a path as blocked from start_time to end_time """
        for time in range(start_time, end_time + 1):
            self.blocked_paths[(room1, room2, time)] = True


def get_accessible_rooms(current_time, current_room, graph, obstacles):
  """Returns accessible rooms from the current_room"""
  neighbors = []
  for neighbor in graph.get(current_room, []):
      if not obstacles.is_path_blocked(current_room, neighbor, current_time):
        neighbors.append(neighbor)
  return neighbors

def bfs(start, goal, graph, obstacles):
    queue = [(start, 0, [start])]  # (room, time, path)
    visited = set()

    while queue:
        current_room, current_time, path = queue.pop(0)
        if current_room == goal:
          return path # return path
        
        if (current_room, current_time) in visited:
            continue
        visited.add((current_room, current_time))

        for neighbor in get_accessible_rooms(current_time, current_room, graph, obstacles):
          new_time = current_time + 1  # Advance time
          queue.append((neighbor, new_time, path + [neighbor]))
    return None # No path was found



if __name__ == "__main__":
    # Define graph (rooms and corridors)
    castle_graph = {
        "Great Hall": ["Potions Classroom", "Library", "Entrance"],
        "Potions Classroom": ["Great Hall", "Dungeons"],
        "Library": ["Great Hall", "Restricted Section"],
        "Restricted Section": ["Library"],
        "Dungeons": ["Potions Classroom", "Secret Passage"],
        "Secret Passage": ["Dungeons"],
        "Entrance": ["Great Hall"]
    }

    # Setup obstacles
    obstacles = Obstacles()
    obstacles.set_block_time("Great Hall", "Library", 3, 5)  # Block from time 3 to 5
    obstacles.set_block_time("Dungeons", "Secret Passage", 1, 2)  # Block from time 1 to 2

    start_room = "Entrance"
    end_room = "Secret Passage"
    path = bfs(start_room, end_room, castle_graph, obstacles)

    if path:
        print(f"Shortest path from {start_room} to {end_room}: {path}")
    else:
        print(f"No path found from {start_room} to {end_room}")