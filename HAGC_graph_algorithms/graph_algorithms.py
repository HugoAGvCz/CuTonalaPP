class Algorithms:
    def __init__(self, graph):
        self.graph = graph
        self.visited = False
    
    def bfs(self, start_node):
        print("*** BFS ***")
        if start_node not in self.graph:
            print("Node not found in graph")
            return -1
        
        visited_nodes = []
        queue = [start_node]
        
        while queue:
            node = queue.pop(0)
            if node not in visited_nodes:
                visited_nodes.append(node)

                for neighbor in self.graph[node]:
                    if neighbor not in visited_nodes:
                        queue.append(neighbor)
        return visited_nodes

    def dfs(self, start_node):
        stack = [start_node]
        visited_node = set()
        path = []

        while stack:
            current = stack.pop()
            
            if current not in visited_node:
                visited_node.add(current)
                path.append(current)

                for neighbor in self.graph[current]:
                    if neighbor not in visited_node:
                        stack.append(neighbor)

        return path


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'E'],
        'D': ['B', 'F'],
        'E': ['B', 'C', 'F'],
        'F': ['D', 'E']
    }

    my_instance = Algorithms(graph) 
    
    result_bfs = my_instance.bfs('D');
    print("BFS algorithm path: ", result_bfs)

    result_dfs = my_instance.dfs('D');
    print("DFS algorithm path: ", result_dfs)