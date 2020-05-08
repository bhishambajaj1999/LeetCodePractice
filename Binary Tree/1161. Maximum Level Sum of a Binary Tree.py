# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        s = [0]*100
        
        def trav(node,lvl):
            s[lvl] += node.val
            if node.left:
                trav(node.left,lvl+1)
            if node.right:
                trav(node.right,lvl+1)
        
        trav(root,0)
        return s.index(max(s)) + 1
