# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.max=0
        self.dfs(root)
        return self.max
        
        
    def dfs(self,root):
        if not root:
            return 0
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        
        self.max=max(self.max,left+right)
        return 1+max(left,right)