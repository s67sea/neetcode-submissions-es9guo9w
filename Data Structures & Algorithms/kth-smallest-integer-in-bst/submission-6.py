# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = None

        def dfs(root):
            nonlocal counter, res

            #if we finished stop recursing
            if res is not None:
                return

            if not root:
                return

            # in-order traversal

            dfs(root.left)
            
            counter += 1
            if counter == k:
                res = root.val
                return

            dfs(root.right)
        
        dfs(root)
        return res
        