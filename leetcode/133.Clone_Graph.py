"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        M = {}
        if not node:
            return None
        def clone_graph(node: Optional['Node']) -> Optional['Node']:
            if node in M:
                return M[node]
            new_node = Node(node.val)
            M[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(clone_graph(neighbor))
            return new_node
        return clone_graph(node)
        
