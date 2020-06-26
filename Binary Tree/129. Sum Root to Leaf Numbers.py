# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        s,r = [(root,root.val)],0
        
        while s:
            node, v = s.pop()
            if node:
                if not node.left and not node.right:
                    r += v
                if node.left:
                    s.append((node.left, 10 * v + node.left.val))
                if node.right:
                    s.append((node.right, 10 * v + node.right.val))

        
        return r
