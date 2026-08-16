# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        numAtLevel = 1

        while q:
            numAtCurrLevel = 0
            for i in range(numAtLevel):
                node = q.popleft()
                if i == numAtLevel-1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                    numAtCurrLevel += 1
                if node.right:
                    q.append(node.right)
                    numAtCurrLevel += 1
                
            numAtLevel = numAtCurrLevel
        
        return res


        