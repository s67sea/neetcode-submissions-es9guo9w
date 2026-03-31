# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def dfs(root,minAllowed,maxAllowed):
            nonlocal valid
            if not root:
                return 
            if not (minAllowed <= root.val <= maxAllowed):
                valid = False
                return
            dfs(root.left,minAllowed,root.val-1)
            dfs(root.right,root.val+1,maxAllowed)
        dfs(root,float('-inf'),float('inf'))
        return valid
