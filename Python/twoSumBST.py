class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        hashset=set()
        return self.bstSearch(root,k,hashset)
    
    def bstSearch(self,root,k,hashset):
        if not root:
            return False
        
        if k-root.val in hashset:
            return True
        
        hashset.add(root.val)
        
        return self.bstSearch(root.left,k,hashset) or self.bstSearch(root.right,k,hashset)