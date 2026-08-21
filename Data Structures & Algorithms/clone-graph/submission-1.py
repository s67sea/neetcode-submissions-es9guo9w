"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #cloning a node is akin to visiting
        #if we've already cloned the node we know we've done that path
        if not node:
            return None

        hm = {}

        def dfs(node):
            if node in hm:
                return hm[node]
            
            nodecopy = Node(node.val)
            hm[node] = nodecopy
            neighbourlistcopy = [] 
            for neighbour in node.neighbors:
                neighbourcopy = dfs(neighbour)
                neighbourlistcopy.append(neighbourcopy)
                
            nodecopy.neighbors = neighbourlistcopy
            return nodecopy
        
        return dfs(node)

