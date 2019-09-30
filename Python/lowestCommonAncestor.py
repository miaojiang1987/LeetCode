class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        
        if root==q or root==p:
            return root
        
        
        left=self.lowestCommonAncestor(root.left,p,q)
        
        right=self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right