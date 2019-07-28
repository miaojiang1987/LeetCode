# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.maxdiff=0
        self.dfs(root,root.val,root.val)
        return self.maxdiff
        
        
    
    def dfs(self,node,minimum,maximum):
        if not node:
            return;
        
        diff1 = abs(node.val-minimum);
        diff2 = abs(node.val-maximum);
        self.maxdiff = max(self.maxdiff, diff1);
        self.maxdiff = max(self.maxdiff, diff2);
        self.dfs(node.left, min(minimum, node.val),max(maximum, node.val));
        self.dfs(node.right,min(minimum, node.val),max(maximum, node.val));