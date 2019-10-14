# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max=float('-inf')
        self.dfs(root)
        return self.max
    
    def dfs(self,root):
        if not root:
            return 0
        left_result=max(self.dfs(root.left),0)
        right_result=max(self.dfs(root.right),0)
        
        self.max=max(self.max,root.val+left_result+right_result)
        
        return max(root.val+left_result,root.val+right_result)