# Case Study

## Pokemon

This case study integrates the engaging world of Pokémon with fundamental AI concepts, making it an exciting and educational experience for BTech students. By using AI techniques such as search algorithms, optimization methods, and adversarial strategies, students can develop a deeper understanding of problem-solving and computational thinking.

### 1. Breadth-First Search (BFS): Exploring the Castle [(Link to program)](bfs.py)

#### Narrative

You are an aspiring Pokémon trainer exploring a maze-like Pokémon Sanctuary. Your goal is to capture a specific Pokémon hidden in one of the sanctuary’s rooms. Each room is connected to others via doors, and movement is restricted to one step at a time.

#### Task

Use BFS to determine the shortest sequence of rooms to traverse from the starting point to the room containing the target Pokémon.

#### Challenges:

• Ensure the solution explores all possible paths systematically.

• Handle multiple Pokémon in different rooms and find the shortest path to the first one encountered.

#### Extension

Add traps in certain rooms that make them temporarily inaccessible, requiring re-exploration once the trap is deactivated.

### Algorithm Flowchart

1. Start at the initial room.

2. Add the starting room to a queue and mark it as visited.

3. Explore each neighboring room systematically.

4. If a target Pokémon is found, reconstruct and return the shortest path.

5. If the queue is empty and no Pokémon is found, return "No Pokémon Found."

### Output

Shortest Path: ['A', 'B', 'E', 'G']

---

### 2. Bidirectional Search: Triwizard Maze [(Link to program)](bidirectional.py)

#### Narrative

You are trying to reach a Pokémon Battle Arena starting from two points—your current location and the arena's entrance. Multiple paths exist, some of which are blocked.

#### Task

Use bidirectional search to find the fastest route from your location to the arena.

#### Challenges:

• Ensure that both search directions meet at the shortest path intersection.

• Handle dynamic obstacles that can block or unblock during the search.

#### Extension

Add teleportation points that can drastically change the search path.

### Algorithm Flowchart

1. Initialize two queues: one from the starting position and one from the goal.

2. Expand nodes alternately from both directions.

3. If a common node is found in both search trees, reconstruct the shortest path.

4. Handle dynamic obstacles by adjusting the search path dynamically.

### Output

Shortest Path to Arena: ['A', 'B', 'E', 'G', 'H']

---

### 3. Simulated Annealing: Wand Customization [(Link to program)](simulated-annealing.py)

#### Narrative

Devise a strategy for evolving your Pokémon, considering both immediate experience gains and long-term benefits.

#### Task

Use simulated annealing to optimize the evolution plan, balancing exploration and exploitation.

#### Challenges:

• Tune the cooling schedule to balance computation time and solution quality.

• Handle random events like surprise battles that affect experience.

#### Extension

Incorporate additional variables like evolution stones or held items.

### Algorithm Flowchart

1. Define an initial solution.

2. Calculate its cost.

3. Generate a neighboring solution.

4. Accept the neighbor based on temperature-based probability.

5. Reduce the temperature gradually until the system stabilizes.

6. Return the best solution found.

### Output

Optimized Evolution Plan: ['Train', 'Evolve', 'Use Item', 'Train', 'Train']
