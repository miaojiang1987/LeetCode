# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        
        if root==p or root==q:
            return root
        
        left_root=self.lowestCommonAncestor(root.left,p,q)
        right_root=self.lowestCommonAncestor(root.right,p,q)
        
        if left_root and right_root:
            return root
        
        if left_root:
            return left_root
        
        if right_root:
            return right_root