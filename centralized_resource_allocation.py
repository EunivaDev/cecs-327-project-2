class Task:
    def __init__(self, id, priority, cpu_requirement):
        self.id = id
        self.priority = priority
        self.cpu_requirement = cpu_requirement

class CentralScheduler:
    def __init__(self, total_cpu_capacity):
        self.total_cpu_capacity = total_cpu_capacity
        self.available_cpu_capacity = total_cpu_capacity

    def allocate_resources(self, tasks):
        tasks.sort(key=lambda x: x.priority, reverse=True)  # Sort tasks by priority (higher priority first)
        for task in tasks:
            if task.cpu_requirement <= self.available_cpu_capacity:
                print(f"Allocating {task.cpu_requirement} CPU units to Task {task.id}")
                self.available_cpu_capacity -= task.cpu_requirement
            else:
                print(f"Insufficient CPU resources to allocate to Task {task.id}")

    def compare_and_analyze(self):
        # Simulate comparison and analysis
        print("Comparison and Analysis:")
        print("- Simplicity: Centralized allocation is simpler to implement compared to distributed and elastic approaches.")
        print("- Scalability: Centralized allocation may become a bottleneck as the system scales compared to distributed and elastic approaches.")
        print("- Fault Tolerance: Centralized allocation has a single point of failure compared to distributed and elastic approaches.")
        print("- Flexibility: Centralized allocation is less flexible compared to distributed and elastic approaches.")
        print("- Performance: Centralized allocation may have lower performance under high workload compared to distributed and elastic approaches.")

# Example usage:
if __name__ == "__main__":
    # Create tasks with priority and CPU requirements
    tasks = [
        Task(id=1, priority=3, cpu_requirement=5),
        Task(id=2, priority=2, cpu_requirement=4),
        Task(id=3, priority=1, cpu_requirement=3)
    ]

    # Create a central scheduler with total CPU capacity
    scheduler = CentralScheduler(total_cpu_capacity=10)

    # Allocate resources to tasks
    scheduler.allocate_resources(tasks)

    # Perform comparison and analysis
    scheduler.compare_and_analyze()

