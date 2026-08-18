# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if not root:
                res += "N,"
                return
            res += str(root.val)
            res += ","
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ptr = 0
        order = data.split(",")

        def dfs():
            nonlocal ptr
            if ptr >= len(order):
                return 
            if order[ptr]=="N":
                ptr += 1
                return None
            
            root = TreeNode(order[ptr])
            ptr += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()