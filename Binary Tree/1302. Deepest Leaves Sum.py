# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# BFS


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        f = [root]
        r = 0
        while f:
            t = []
            r = 0
            for node in f:
                r += node.val
                if node.left: t += [node.left]
                if node.right: t += [node.right]
            f = t
        return r
