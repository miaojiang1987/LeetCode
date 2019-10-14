# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root,sum)
    
    
    def dfs(self,root,target):
        if not root:
            return False
        if root.val==target and not root.left and not root.right:
            return True
        remain=target-root.val
        
        return self.dfs(root.left,remain) or self.dfs(root.right,remain)