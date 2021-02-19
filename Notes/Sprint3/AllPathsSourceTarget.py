"""
All Paths from Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).
"""

from collections import deque

class Solution:
    """
    Understand

    Plan
    1. Translate the problem into graph terminology
    vertex - each index in the list
    edges - the list of values in a specified index
    weights - n/a

    2. Build your graph
    [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],]
    
    2.1 Build Explicit graph
    No need to build explicit graph, just index properly into the input array to get the
    neighbors of the current node
    input = [[1,2], [3], [3], []]
    0: {1,2}
    1: {3}
    2: {3}
    3: {}

    2.2 Traverse given list
    We need to do a traversal
    It doesn't matter what type of traversal
    Use a stack to do a DFT on the graph
    Keep track of the current path that we've taken

    If we find the destination node, append the path we took to the resulting array

    Return the resulting array at the end

    stack = 1, 2 (values in input 0/node 0 neighbors)
    currNode = 0
    """


    def allPathsSourceTarget(self, graph):
        stack = deque()
        stack.append((0, [0]))
        res = []
        destinationNode = len(graph) - 1
        
        while len(stack) > 0:
            curr = stack.pop()
            currNode, currPath = curr[0], curr[1]
            if currNode == destinationNode:
                res.append(currPath)
            else:
                for neighbor in graph[currNode]:
                    newPath = currPath.copy()
                    newPath.append(neighbor)
                    stack.append((neighbor, newPath))
        return res

    ### alternative solution
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.allPathsSourceTargetHelper(graph, len(graph) - 1, 0, [0], res)
        return res
    
    def allPathsSourceTargetHelper(self, graph, destinationNode, currNode, currPath, res):
        # base-case: reached destination node
        if currNode == destinationNode:
            res.append(currPath)
        else:
            for neighbor in graph[currNode]:
                newPath = currPath.copy()
                newPath.append(neighbor)
                self.allPathsSourceTargetHelper(graph, destinationNode, neighbor, newPath, res)