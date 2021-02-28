# Adjacency Matrix

grah_matrix = [
    [0,1,0,0,0],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,0,0]
]

# What are my neigbors for A?
# graph_matrix[0] # <- All the neighbors for A

# # Is B and C connected?
# graph_matrix[1][2] == 1 # return true

# # Add connection from A to C
# graph_matrix[0][2] = 1 # we have now made a connection from A to C


# Adjacency List

graph_list = {
    'A': {'B'},
    'B': {'C', 'D', 'E'},
    'C': {'D'},
    'D': {},
    'E': {}
}

# # What are my neighbors for A?
# graph_list['A'] # <- the set of all neighbors for A

# # Is C and B connected?
# 'C' in graph_list['B'] # ? this will return true

# # Add connection from A to C
# graph_list['A'].add['C']

# Add a new vertex and connect A and C to it
graph_list['F'] = {'C'}
graph_list['A'].add('F')


def print_paths(graph, start_vertex, current_path=[]):
    current_path.append(start_vertex)

    # if no neighbors, print the path
    if len(graph[start_vertex]) == 0:
        print(current_path)

    # For each neighbor, call print_paths, with the current_path containing our current_vertex
    for neighbor in graph[start_vertex]:
        # make a copy of the path
        new_path = current_path.copy()
        print_paths(graph, neighbor, new_path)

print_paths(graph_list, "A", [])