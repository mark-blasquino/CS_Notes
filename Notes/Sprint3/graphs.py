graph = {
    "A": {"B", "C", "F"},
    "B": {"E"},
    "C": {"D"},
    "D": {"A", "G"},
    "E": {},
    "F": {},
    "G": {}
}

def bfs(start_vertex, graph, goal_vertex):
    # create a queue
    queue = []
    # create a visited set
    visited_set = set()
    # throw the start vertex onto the queue
    queue.insert(0, start_vertex)
    # while the queue is not empty
    while len(queue) > 0:
        # take the first item off the queue
        item = queue.pop()
        # Add the item, to the visited set
        visited_set.add(item)

        # do whatever it is you need to to the item
        print(item)
        # check if this item is the goal, and if so, end the search

        # Add all neighbors to the queue that we have NEVER seen yet
        # get the neighbors
        neighbors = graph[item]
        for neighbor in neighbors:
            # have I seen this neighbor before?
                # If yes, skip them
            if neighbor not in visited_set:
                # for each of them, add them to the queue
                queue.insert(0, neighbor)
        
    
# bfs('A', graph, 'D')

def dfs(start_vertex, graph, goal_vertex):
    # create a queue
    stack = []
    # create a visited set
    visited_set = set()
    # throw the start vertex onto the queue
    stack.append(start_vertex)
    # while the queue is not empty
    while len(stack) > 0:
        # take the first item off the queue
        item = stack.pop()
        # Add the item, to the visited set
        visited_set.add(item)

        # do whatever it is you need to to the item
        print(item)
        # check if this item is the goal, and if so, end the search

        # Add all neighbors to the queue that we have NEVER seen yet
        neighbors = graph[item]
        # get the neighbors
        for neighbor in neighbors:
            # have I seen this neighbor before?
                # If yes, skip them
            if neighbor not in visited_set:
                # for each of them, add them to the queue
                stack.append(neighbor)

# dfs('A', graph, 'D')


def recursive_dfs(current_vertex, graph, visited_set):
    # add the current_vertex to visited set
    visited_set.add(current_vertex)
    # print the current_node
    print(current_vertex)

    # get the neighbors
    neighbors = graph[current_vertex]
    # for each neighbor, recurse on them if they are not in the visited set
    for neighbor in neighbors:
        if neighbor not in visited_set:
            recursive_dfs(neighbor, graph, visited_set)

recursive_dfs('A', graph, set())