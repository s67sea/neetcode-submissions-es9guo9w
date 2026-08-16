# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p,q are too big then it's in the right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        #if p,q are too small then it's in the left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        # else it's curr
        return root