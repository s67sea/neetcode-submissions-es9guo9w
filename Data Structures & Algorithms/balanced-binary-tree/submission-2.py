# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True 
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0

            nonlocal res

            #dfs should always return the height
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)

            if abs(left-right) > 1:
                res = False
            
            return max(left,right)
        
        dfs(root)
        return res
            
            