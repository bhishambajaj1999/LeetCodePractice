# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(root):
            if not root:
                return 0
            if L <= root.val <= R:
                self.s += root.val
            
            if L < root.val:
                dfs(root.left)
            
            if root.val < R:
                dfs(root.right)
            
        self.s = 0
        dfs(root)
        return self.s
