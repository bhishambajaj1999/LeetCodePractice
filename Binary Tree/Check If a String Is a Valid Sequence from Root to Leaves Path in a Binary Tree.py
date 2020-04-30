# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def existPath(root, arr, index): 
      
            if (root == None or index >= len(arr)): 
                return False
            
            if root.left == None and root.right == None:
                return root.val == arr[index] and index == len(arr) - 1
            
            if root.val == arr[index]:
                return existPath(root.left,arr,index+1) or existPath(root.right, arr,index+1)
            
            return False
            
        
        return existPath(root, arr, 0)
