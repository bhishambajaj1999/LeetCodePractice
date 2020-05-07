# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        res = []
        
        def dfs(node,parent,lvl):
            if not node or len(res) == 2:
                return
            else:

                if node.val == x or node.val == y:
                    res.append((parent,lvl))

                dfs(node.left,node,lvl+1)
                dfs(node.right,node,lvl+1)
        
        dfs(root,None,0)
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]

