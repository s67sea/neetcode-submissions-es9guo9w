# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = deque()
        q.append(root)
        numAtLevel = 1
        res = []

        while q:
            levelres = []
            numAtNewLevel = 0
            for _ in range(numAtLevel):
                node = q.popleft()
                levelres.append(node.val)
                if node.left:
                    q.append(node.left)
                    numAtNewLevel += 1
                if node.right:
                    q.append(node.right)
                    numAtNewLevel += 1
            numAtLevel = numAtNewLevel
            res.append(levelres)

        return res

