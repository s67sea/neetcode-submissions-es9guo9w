# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        bestSum = float("-inf")
        #every valid path must go through a given root node
        #we can calculate the best we can do on the LHS and the best we can do on the RHS
        #and we can make the active choice to include or not include the lhs/rhs depending on what is optimal
        #we should not include negative numbers. the "best sum". of a subtree is always 

        #if a path sum is negative we should just return 0

        #the return value should be the best single-path sum (without dual branching)

        def dfs(root: Optional[TreeNode]):
            nonlocal bestSum 

            if not root:
                return 0
            
            #get the best path from the left side
            lhs = dfs(root.left)
            #get the best path from the right side
            rhs = dfs(root.right)

            #if the optimal path is here, we have options
            opt1 = root.val + lhs
            opt2 = root.val + rhs
            opt3 = root.val + lhs + rhs
            opt4 = root.val

            bestSum = max(bestSum, opt1, opt2, opt3, opt4)

            #the best path we can return through here is
            lhspathsum = max(lhs,0) + root.val
            rhspathsum = max(rhs,0) + root.val
            return max(lhspathsum, rhspathsum)
        
        dfs(root)
        return bestSum

