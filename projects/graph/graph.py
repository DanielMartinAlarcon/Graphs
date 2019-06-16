"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.colors = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        self.colors[vertex] = 'white'

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            print("v1 is not a valid vertex")
        elif v2 not in self.vertices:
            print("v2 is not a valid vertex")
        else:
            self.vertices[v1].add(v2)
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited_nodes = []
        while q.size() > 0:
            current_node = q.dequeue()
            
            if self.colors[current_node] == 'white':
                self.colors[current_node] = 'gray'
                visited_nodes.append(current_node)
                
            for node in self.vertices[current_node]:
                if self.colors[node] == 'white':
                    q.enqueue(node)
        
        # Reset colors
        for vertex in self.colors:
            self.colors[vertex] = 'white'

        return visited_nodes

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited_nodes = []
        while stack.size() > 0:
            current_node = stack.pop()

            if self.colors[current_node] == 'white':
                self.colors[current_node] = 'gray'
                visited_nodes.append(current_node)

            for node in self.vertices[current_node]:
                if self.colors[node] == 'white':
                    stack.push(node)

        # Reset colors
        for vertex in self.colors:
            self.colors[vertex] = 'white'

        return visited_nodes

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if self.colors[starting_vertex] == 'white':
            self.colors[starting_vertex] = 'gray'
            print('dft_rec ', starting_vertex)

            for node in self.vertices[starting_vertex]:
                self.dft_recursive(node)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Reset all nodes to white
        for v in self.colors:
            self.colors[v] = 'white'

        q = Queue()
        q.enqueue(starting_vertex)
        all_paths = {v:[] for v in self.vertices}

        # Initialize for first node
        all_paths[starting_vertex].append(starting_vertex)
        self.colors[starting_vertex] = 'gray'

        while q.size() > 0:
            parent = q.queue[0]
            
            for child in self.vertices[parent]:
                if self.colors[child] == 'white': 
                    self.colors[child] = 'gray'
                    # Add to the queue
                    q.enqueue(child)
                    # Create a new path, based on the parent's path
                    all_paths[child] = all_paths[parent] + [child]
                    
            q.dequeue()
            self.colors[parent] = 'black'

        return all_paths[destination_vertex]


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Reset all nodes to white
        for v in self.colors:
            self.colors[v] = 'white'

        stack = Stack()
        stack.push(starting_vertex)
        all_paths = {v:[] for v in self.vertices}

        # Initialize for first node
        all_paths[starting_vertex].append(starting_vertex)
        self.colors[starting_vertex] = 'gray'

        while stack.size() > 0:
            parent = stack.pop()
            
            for child in self.vertices[parent]:
                if self.colors[child] == 'white': 
                    self.colors[child] = 'gray'
                    stack.push(child)
                    # Create a new path, based on the parent's path 
                    all_paths[child] = all_paths[parent] + [child]
                    
            self.colors[parent] = 'black'

        return all_paths[destination_vertex]
        


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('\nVertices: ', graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\nDFT: ', graph.dft(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('\nBFT: ', graph.bft(1))

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nRecursive DFT:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('\nBreadth-first search (1 to 6): ')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('\nDepth-first search (1 to 6): ')
    print(graph.dfs(1, 6))
