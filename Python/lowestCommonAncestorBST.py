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
        
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        elif root.val<q.val and root.val<p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        else:
            return root