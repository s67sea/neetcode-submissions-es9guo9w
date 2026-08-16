# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root: Optional[TreeNode], maxsofar: int):
            #dfs should basically return maxsofar
            nonlocal res

            if not root:
                return

            #if this node is >= max in path from root, mark as good
            if root.val >= maxsofar:
                res += 1
            
            #process children
            #update maxsofar to include the current node
            maxsofar = max(root.val, maxsofar)
            if root.left:
                dfs(root.left,maxsofar)
            if root.right:
                dfs(root.right, maxsofar)
        
        dfs(root, float("-inf"))
        return res
            

        