# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        self.helper(root,result)
        return result
    
    def helper(self,root,result):
        if root:
            if root.left:
                self.helper(root.left,result)
            result+=[root.val]
            if root.right:
                self.helper(root.right,result)