# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root,float('-inf'),float('inf'))
    
    
    def helper(self,node,lower,upper):
        if not node:
            return True
        val=node.val
        if val<=lower or val>=upper:
            return False
        
                
        if not self.helper(node.right,val,upper):
            return False
        
        if not self.helper(node.left,lower,val):
            return False

        
        return True