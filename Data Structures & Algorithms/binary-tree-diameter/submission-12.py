# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]):
            nonlocal res 

            if not root:
                return 0
            
            #compute max height of subtrees; diam is sum + 1
            left = dfs(root.left)
            right = dfs(root.right)

            diam = left + right
            res = max(res, diam)

            return max(left,right) + 1
        
        dfs(root)

        return res

        
        