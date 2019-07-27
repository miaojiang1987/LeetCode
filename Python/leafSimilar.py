# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1=[]
        leaves2=[]
        
        self.dfs(root1,leaves1)
        self.dfs(root2,leaves2)
        
        return leaves1==leaves2
    
    def dfs(self,node,leaves):
        if not node:
            return
        
        if not node.left and not node.right:
            leaves.append(node.val)
        
        self.dfs(node.left,leaves)
        self.dfs(node.right,leaves)