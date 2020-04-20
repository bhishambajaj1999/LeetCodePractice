# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, A: List[int]) -> TreeNode:
        def helpf(i,j):
            if i==j: return
            
            root = TreeNode(A[i])            
            mid = bisect.bisect(A,A[i],i+1,j)
            
            root.left = helpf(i+1,mid)
            root.right = helpf(mid,j)
            
            return root
        return helpf(0,len(A))
