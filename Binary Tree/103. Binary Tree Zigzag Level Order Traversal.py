class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def zigzagLevelOrder(root: TreeNode):
        if not root: return []
        
        q = [root]
        m,n,f = [],[],-1
        
        while(q):
            m = []
            for i in range(len(q)):
                t = q.pop(0)
                m.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            f *= -1
            n += [m[::f]]
        
        return n

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(zigzagLevelOrder(root))
