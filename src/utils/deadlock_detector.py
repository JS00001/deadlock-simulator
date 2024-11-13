from collections import defaultdict

class DeadlockDetector:
    def __init__(self):
        self.held_resources = defaultdict(list)
        self.requested_resources = defaultdict(list)
        
    # Give a resource to a process
    def allocate_resource(self, process_id, resource_id):
        self.held_resources[process_id].append(resource_id)
        
    # Request a resource for a process
    def request_resource(self, process_id, resource_id):
        self.requested_resources[process_id].append(resource_id)

    # Release a resource held by a process
    def release_resource(self, process_id, resource_id):
        if resource_id in self.held_resources[process_id]:
            self.held_resources[process_id].remove(resource_id)
        else:
            print(f"{process_id} does not hold {resource_id}")
        
    # Use a wait-for graph to detect deadlock, and return the processes involved
    # in the deadlock
    def detect_deadlock(self):
        # Build wait-for graph
        graph = defaultdict(set)

        # For each process, see what resources it wants, and find the owner of those resources
        for process1 in self.requested_resources:
            for resource in self.requested_resources[process1]:
                for process2, resources in self.held_resources.items():
                    if resource in resources and process1 != process2:
                        graph[process1].add(process2)
        
        # Find circular dependencies in the graph
        def dfs(node, path):
            # If we find a dependency cycle, return the cycle
            if node in path:
                cycle_start = path.index(node)
                return path[cycle_start:]
            
            # Otherwise, keep searching
            for next_node in graph[node]:
                result = dfs(next_node, path + [node])
                if result:
                    return result
                
            # If no circular dependency is found, return an empty list
            return []
            
        # For each process, check for a circular dependency
        for process in list(graph.keys()):
            circ = dfs(process, [])

            if circ:
                return circ
                
        return []
        
    # Release the resources held by the first process in the deadlock
    def resolve_deadlock(self, processes):
        if not processes:
            return
            
        victim = processes[0]
        
        # Release all of the resources held by the victim
        self.held_resources[victim] = []
        self.requested_resources[victim] = []
        print(f"Fixed deadlock by releasing {victim}'s resources")
