class Solution(object):
    def flatten(self, root):
        if root is None: return root
        self.getflatten(root)
 
    def getflatten(self, root):
        if root is None: return
        self.getflatten(root.left)
        self.getflatten(root.right)
        current=root.left
        if current is None:
            return
        while current.right is not None:
            current=current.right
        current.right=root.right
        root.right=root.left
        root.left=None