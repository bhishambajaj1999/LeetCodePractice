# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root: return None
        q = deque()
        q.append(root)
        while q:
            t = q.popleft()
            t.left,t.right = t.right,t.left     
            if t.left: q.append(t.left)
            if t.right: q.append(t.right)
        return root

        
