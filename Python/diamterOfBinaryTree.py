class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max=0
        self.depth(root)
        return self.max
        
    
    def depth(self,root):
        if not root:
            return 0
        L=self.depth(root.left)
        R=self.depth(root.right)
        
        self.max=max(self.max,L+R)
        return max(L,R)+1