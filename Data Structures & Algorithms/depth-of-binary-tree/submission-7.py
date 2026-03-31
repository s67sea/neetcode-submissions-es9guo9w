# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1+max(dfs(root.left),dfs(root.right))
        # return dfs(root)

        def bfs(root):
            level = 0
            q = deque()
            if root:
                q.append(root)
            while q:
                n = len(q)
                #process this level
                for i in range(n):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1
            return level
        return bfs(root)
            