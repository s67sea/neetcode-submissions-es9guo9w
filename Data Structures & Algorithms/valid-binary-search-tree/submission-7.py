# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we should pass down the valid range
        # valid range starts as (-inf, inf)
        # say you need to be STRICTLY outside the valid range

        def dfs(root: Optional[TreeNode], minVal, maxVal):
            if not root: 
                return True
            
            # current node must respect the boundaries
            if not minVal < root.val < maxVal:
                return False
            
            # process children; must respect the boundaries 
            left = dfs(root.left,minVal,root.val) if root.left else True
            right = dfs(root.right,root.val,maxVal) if root.right else True
            return left and right
        
        return dfs(root,float("-inf"),float("inf"))



            
            

