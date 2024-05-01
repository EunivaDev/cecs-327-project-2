# Define the Task class
import random

class Task:
    def __init__(self, id, priority, cpu_requirement):
        self.id = id
        self.priority = priority
        self.cpu_requirement = cpu_requirement

# Define the Node class
class Node:
    def __init__(self, id, cpu_capacity):
        self.id = id
        self.cpu_capacity = cpu_capacity
        self.available_cpu_capacity = cpu_capacity

    def negotiate_resources(self, tasks):
        if tasks.cpu_requirement <= self.available_cpu_capacity:
            self.available_cpu_capacity -= tasks.cpu_requirement
            print(f"CPU {self.id} is executing Task {tasks.id} with using resource of {tasks.cpu_requirement}")
            return True
        else:
            print(f"CPU {self.id} cannot execute Task {tasks.id} due to insufficient resources")
            return False

    def compare_and_analyze(self):
        # Simulate comparison and analysis
        print("Comparison and Analysis:")
        print("- Simplicity: Distributed allocation may be more complex to implement compared to centralized allocation.")
        print("- Scalability: Distributed allocation can scale better than centralized allocation as the system grows.")
        print("- Fault Tolerance: Distributed allocation provides better fault tolerance compared to centralized allocation.")
        print("- Flexibility: Distributed allocation offers greater flexibility compared to centralized allocation.")
        print("- Performance: Distributed allocation may have better performance under high workload compared to centralized allocation.")

def distribute_tasks(nodes, tasks):
    tasks.sort(key=lambda x: x.priority, reverse=True) #sorting tasks
    for task in tasks:
        assigned = False
        while not assigned:
            node = random.choice(nodes)
            assigned = node.negotiate_resources(task)
            if assigned:
                print(f"Task {task.id} is assigned to CPU {node.id}")

# Define sample tasks
tasks = [
    Task(id=1, priority=3, cpu_requirement=5),
    Task(id=2, priority=2, cpu_requirement=4),
    Task(id=3, priority=1, cpu_requirement=3)
]

# Example usage:
if __name__ == "__main__":
    # Create nodes with CPU capacities
    nodes = [
        Node(id=1, cpu_capacity=5),
        Node(id=2, cpu_capacity=4),
        Node(id=3, cpu_capacity=3)
    ]

    distribute_tasks(nodes, tasks)

    # Distribute tasks among nodes and negotiate resource allocation
    #for node in nodes:
        #node.negotiate_resources(tasks)

    # Perform comparison and analysis
    #nodes[0].compare_and_analyze()  # Perform analysis on one of the nodes
