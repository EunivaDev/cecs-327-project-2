import time  # Import the time module

class ElasticResourceManager:
    def __init__(self, initial_capacity):
        self.current_capacity = initial_capacity

    def adjust_capacity(self, new_capacity):
        print(f"Adjusting capacity from {self.current_capacity} to {new_capacity}")
        self.current_capacity = new_capacity

    def compare_and_analyze(self):
        # Simulate comparison and analysis
        print("Comparison and Analysis:")
        print("- Simplicity: Elastic provisioning may be more complex to implement compared to centralized and distributed allocation.")
        print("- Scalability: Elastic provisioning provides dynamic scalability, adapting to changing workload conditions.")
        print("- Fault Tolerance: Elastic provisioning can enhance fault tolerance by dynamically adjusting resources in response to failures.")
        print("- Flexibility: Elastic provisioning offers flexibility to scale resources based on demand.")
        print("- Performance: Elastic provisioning may improve overall system performance by optimizing resource utilization.")

# Example usage:
if __name__ == "__main__":
    # Create an elastic resource manager with initial capacity
    resource_manager = ElasticResourceManager(initial_capacity=10)

    # Simulate dynamic capacity adjustment
    time.sleep(3)  # Simulate workload change
    resource_manager.adjust_capacity(new_capacity=15)

    # Perform comparison and analysis
    resource_manager.compare_and_analyze()

