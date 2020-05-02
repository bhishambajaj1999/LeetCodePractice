# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        def checklvl(node,dep):
            if node:
                if dep == len(view):
                    view.append(node.val)
                checklvl(node.right,dep+1)
                checklvl(node.left,dep+1)
        
        view = []
        checklvl(root,0)
        return view
