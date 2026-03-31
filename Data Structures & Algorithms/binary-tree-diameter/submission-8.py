# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0
        def dfs(root):
            nonlocal maxdiam
            if not root:
                return 0
            lhs = dfs(root.left)
            rhs = dfs(root.right)
            maxdiam = max(maxdiam,lhs+rhs)
            return 1 + max(lhs,rhs)#height of tree
        dfs(root)
        return maxdiam
