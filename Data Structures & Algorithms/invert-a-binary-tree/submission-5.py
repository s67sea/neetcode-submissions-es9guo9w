# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS solution
        #if the root is null, return
        
        if not root: return None

        q = deque()
        q.append(root)

        while q:
            elem = q.popleft()
            elem.left, elem.right = elem.right, elem.left
            if elem.left:
                q.append(elem.left)
            if elem.right:
                q.append(elem.right)
        
        return root

