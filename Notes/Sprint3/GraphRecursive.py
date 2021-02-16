# Pseudocode
"""
procedure DFT(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFT(G, w)
"""
adjList = {
    1: {2, 3},
    2: {4},
    3: {4},
    4: {1}
}

visited = set()

def dftRecursive(startingNode, graph):
    visited.add(startingNode)
    print(startingNode)
    for neighbor in graph[startingNode]:
        if not neighbor in visited:
            dftRecursive(neighbor, graph)

dftRecursive(1, adjList)

# Code 2: removing visited as a glabal variable

def dftRecursive(startingNode, graph):
    visited = set()
    dftRecursiveHelper(startingNode, graph, visited)

def dftRecursiveHelper(node, graph) # 01:34 in recording CSPT17