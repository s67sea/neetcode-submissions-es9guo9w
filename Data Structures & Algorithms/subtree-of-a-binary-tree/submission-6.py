# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            
            left = same(p.left,q.left)
            right = same(p.right,q.right)
            return (left and right)
        
        if same(root,subRoot):
            return True
        if not root:
            return False
        
        # recurse left and right
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return (left or right)