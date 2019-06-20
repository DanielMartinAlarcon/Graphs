import sys
sys.path.insert(0, '/Users/DMA/Repos/Graphs/projects/graph')
from graph import Graph

def ancestors(scion, lineage):
    graph = Graph()
    
    # Populate vertices and edges
    for x in lineage:
        graph.add_vertex(x[0])
        graph.add_vertex(x[1])
    for x in lineage:
        graph.add_edge(x[0], x[1])

    # Create a dictionary of all the descent lines that lead to the scion.
    # Keys are the lengths of these lines,
    # values are lists of all the lines of that length
    bloodlines = {}
    for v in graph.vertices:
        descent_line = graph.dfs(v, scion)
        length = len(descent_line)
        if length not in bloodlines:
            bloodlines[length] = [descent_line]
        else:
            bloodlines[length].append(descent_line)

    max_length = max(bloodlines.keys())
    ealiest_ancestor = min([line[0] for line in bloodlines[max_length]])

    if max_length == 1: 
        return -1
    else: 
        return ealiest_ancestor