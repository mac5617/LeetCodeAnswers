"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        def clone(node):
            if node in seen:
                return seen[node]
            
            copy = Node(node.val)
            seen[node] = copy
            for x in node.neighbors:
                copy.neighbors.append(clone(x))
            return copy
        return clone(node) if node else None