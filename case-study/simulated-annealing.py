import random
import math

def simulated_annealing(initial_solution, cost_function, neighbor_function, initial_temp, cooling_rate):
    current_solution = initial_solution
    current_cost = cost_function(current_solution)
    temperature = initial_temp

    while temperature > 0.00001:
        new_solution = neighbor_function(current_solution)
        new_cost = cost_function(new_solution)
        delta_cost = new_cost - current_cost

        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
          current_solution = new_solution
          current_cost = new_cost

        temperature *= cooling_rate
    return current_solution

# Example usage (not executable)

# Dummy Cost Function
def cost_function(evolution_plan):
    """Calculate the cost of a plan (simulated with random values for example)."""
    cost = 0
    for step in evolution_plan:
      #  Simulated cost calculation
        cost+= random.randint(1, 10)
    return cost

# Dummy Neighbor Function
def neighbor_function(evolution_plan):
    """Generate a neighbor plan by making a random change."""
    neighbor = evolution_plan[:]
    index_to_modify = random.randint(0, len(neighbor) -1)
    neighbor[index_to_modify] = random.choice(['Train','Use Item', 'Evolve'])
    return neighbor


initial_evolution_plan = ['Train', 'Train', 'Use Item', 'Train', 'Evolve', 'Train'] # Define the initial plan
initial_temperature = 100  # Start with a higher temperature
cooling_rate_value = 0.98  # Slow down the cooling
optimized_plan = simulated_annealing(initial_evolution_plan, cost_function, neighbor_function, initial_temperature, cooling_rate_value)
print("Optimized Evolution Plan:", optimized_plan)