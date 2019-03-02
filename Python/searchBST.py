class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        while root:
            if val==root.val:
                return root
            
            elif val>root.val:
                root=root.right
            
            else:
                root=root.left