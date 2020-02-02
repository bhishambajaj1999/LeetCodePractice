# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Inorder Traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        s,i = [],float('-inf')
        while s or root:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            if(root.val <= i):
                return False
            
            i = root.val
            root = root.right
            
        return True
