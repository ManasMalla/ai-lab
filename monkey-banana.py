# Monkey Banana Problem
# Develop AI based intelligent agent to implement monkey banana problem.
# Initial State: Entrance to the room
# Goal State: Monkey catches the banana
# Intermediate State: Identification of the supporting tool to reach goal state

# Goal B: Develop competitive environment by using multi agent consideration, ie, monkey 1, monkey 2, FCFS

import time
import threading

class MonkeyBananaProblem:
    def __init__(self, environment):
        self.environment = environment  # Represents the room setup
        self.monkey_position = "entrance"
        self.banana_position = "center"
        self.tool_position = "corner"
        self.has_tool = False
        self.goal_reached = False

    def move_to(self, position):
        print(f"Monkey is moving to {position}.")
        self.monkey_position = position
        time.sleep(1)  # Simulate time to move

    def pick_up_tool(self):
        if self.monkey_position == self.tool_position:
            print("Monkey picked up the tool.")
            self.has_tool = True
        else:
            print("Tool is not here!")

    def use_tool(self):
        if self.has_tool and self.monkey_position == self.banana_position:
            print("Monkey used the tool to grab the banana!")
            self.goal_reached = True
        else:
            print("Cannot use the tool here!")

    def solve(self):
        print("Starting single-agent problem...")
        self.move_to(self.tool_position)
        self.pick_up_tool()
        self.move_to(self.banana_position)
        self.use_tool()
        if self.goal_reached:
            print("Monkey has reached the goal state!")


class MultiAgentMonkeyBananaProblem:
    def __init__(self, num_agents=2):
        self.agents = [MonkeyBananaProblem(environment={}) for _ in range(num_agents)]
        self.lock = threading.Lock()  # For FCFS handling

    def agent_thread(self, agent_id):
        agent = self.agents[agent_id]
        with self.lock:
            print(f"Monkey {agent_id + 1} starts!")
            agent.solve()
            if agent.goal_reached:
                print(f"Monkey {agent_id + 1} grabbed the banana!")
            print(f"Monkey {agent_id + 1} finished its turn.")

    def solve(self):
        threads = []
        for i in range(len(self.agents)):
            thread = threading.Thread(target=self.agent_thread, args=(i,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()


# Run the Single-Agent Problem
single_agent_problem = MonkeyBananaProblem(environment={})
single_agent_problem.solve()

print("\n=== Multi-Agent Competitive Environment ===\n")

# Run the Multi-Agent Problem
multi_agent_problem = MultiAgentMonkeyBananaProblem(num_agents=2)
multi_agent_problem.solve()
