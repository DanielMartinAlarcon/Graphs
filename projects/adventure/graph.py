"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of nodes mapping labels to edges."""
    def __init__(self):
        self.nodes = {}
        self.colors = {}
    
    def add_node(self, node):
        """
        Add a node to the graph.
        """
        if node not in self.nodes:
            self.nodes[node] = {}
            # self.colors[node] = 'white'

    def add_edge(self, v1, v2, direction):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.nodes:
            print(f"{v1} is not a valid node")    
        elif v2 not in self.nodes:
            print(f"{v2} is not a valid node")
        else:
            self.nodes[v1][direction] = v2
        
    # def bft(self, starting_node):
    #     """
    #     Print each node in breadth-first order
    #     beginning from starting_node.
    #     """
    #     q = Queue()
    #     q.enqueue(starting_node)
    #     visited_nodes = []
    #     while q.size() > 0:
    #         current_node = q.dequeue()
            
    #         if self.colors[current_node] == 'white':
    #             self.colors[current_node] = 'gray'
    #             visited_nodes.append(current_node)
                
    #         for node in self.nodes[current_node]:
    #             if self.colors[node] == 'white':
    #                 q.enqueue(node)
        
    #     # Reset colors
    #     for node in self.colors:
    #         self.colors[node] = 'white'

    #     return visited_nodes

    # def dft(self, starting_node):
    #     """
    #     Print each node in depth-first order
    #     beginning from starting_node.
    #     """
    #     stack = Stack()
    #     stack.push(starting_node)
    #     visited_nodes = []
    #     while stack.size() > 0:
    #         current_node = stack.pop()

    #         if self.colors[current_node] == 'white':
    #             self.colors[current_node] = 'gray'
    #             visited_nodes.append(current_node)

    #         for node in self.nodes[current_node]:
    #             if self.colors[node] == 'white':
    #                 stack.push(node)

    #     # Reset colors
    #     for node in self.colors:
    #         self.colors[node] = 'white'

    #     return visited_nodes

    # def dft_recursive(self, starting_node):
    #     """
    #     Print each node in depth-first order
    #     beginning from starting_node.
    #     This should be done using recursion.
    #     """
    #     if self.colors[starting_node] == 'white':
    #         self.colors[starting_node] = 'gray'
    #         print('dft_rec ', starting_node)

    #         for node in self.nodes[starting_node]:
    #             self.dft_recursive(node)


    # def bfs(self, starting_node, destination_node):
    #     """
    #     Return a list containing the shortest path from
    #     starting_node to destination_node in
    #     breath-first order.
    #     """
    #     # Reset all nodes to white
    #     for v in self.colors:
    #         self.colors[v] = 'white'

    #     q = Queue()
    #     q.enqueue(starting_node)
    #     all_paths = {v:[] for v in self.nodes}

    #     # Initialize for first node
    #     all_paths[starting_node].append(starting_node)
    #     self.colors[starting_node] = 'gray'

    #     while q.size() > 0:
    #         parent = q.queue[0]
            
    #         for child in self.nodes[parent]:
    #             if self.colors[child] == 'white': 
    #                 self.colors[child] = 'gray'
    #                 # Add to the queue
    #                 q.enqueue(child)
    #                 # Create a new path, based on the parent's path
    #                 all_paths[child] = all_paths[parent] + [child]
                    
    #         q.dequeue()
    #         self.colors[parent] = 'black'

    #     return all_paths[destination_node]


    # def dfs(self, starting_node, destination_node):
    #     """
    #     Return a list containing a path from
    #     starting_node to destination_node in
    #     depth-first order.
    #     """
    #     # Reset all nodes to white
    #     for v in self.colors:
    #         self.colors[v] = 'white'

    #     stack = Stack()
    #     stack.push(starting_node)
    #     all_paths = {v:[] for v in self.nodes}

    #     # Initialize for first node
    #     all_paths[starting_node].append(starting_node)
    #     self.colors[starting_node] = 'gray'

    #     while stack.size() > 0:
    #         parent = stack.pop()
            
    #         for child in self.nodes[parent]:
    #             if self.colors[child] == 'white': 
    #                 self.colors[child] = 'gray'
    #                 stack.push(child)
    #                 # Create a new path, based on the parent's path 
    #                 all_paths[child] = all_paths[parent] + [child]
                    
    #         self.colors[parent] = 'black'

    #     return all_paths[destination_node]
        


