# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root, left, right
        # inorder: left, root, right

        #first element of preorder is the root. then find the same value in inorder. the split givees you left/right

        #keep going

        if not preorder:
            return None
        
        hm = {val:i for i, val in enumerate(inorder)} #map the in-order value to an index so we know the splice point

        def construct(preorderMin, preorderMax, inorderMin, inorderMax):
            #min and max are inclusive values
            if preorderMin > preorderMax or inorderMin > inorderMax:
                return None
            
            #make the root
            rootval = preorder[preorderMin]
            root = TreeNode(rootval)

            #lhs size = 
            lhsSize = hm[rootval] - inorderMin

            root.left = construct(preorderMin+1,preorderMin+lhsSize,inorderMin,hm[rootval]-1)

            root.right = construct(preorderMin+1+lhsSize,preorderMax,hm[rootval]+1,inorderMax)

            return root
        
        n = len(preorder)
        return construct(0,n-1,0,n-1)


