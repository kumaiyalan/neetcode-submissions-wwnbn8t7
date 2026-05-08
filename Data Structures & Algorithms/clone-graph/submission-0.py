"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def clone(node):
            if node is None:
                return
            if node.val in clones:
                return clones[node.val]
            else:
                cNode = Node(node.val, [])
                clones[node.val] = cNode
                for neighbor in node.neighbors:
                    cNode.neighbors.append(clone(neighbor))
                return cNode
        return clone(node)