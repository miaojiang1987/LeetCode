# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, cur_depth=0):
        if root is None:
            return (cur_depth, root)
        if ((root.left is None) and (root.right is None)):
            return (cur_depth, root)
        if root.left is None:
            return self.helper(root.right, cur_depth+1)
        if root.right is None:
            return self.helper(root.left, cur_depth+1)
        l_h,l_r = self.helper(root.left, cur_depth+1)
        r_h,r_r = self.helper(root.right, cur_depth+1)
        if l_h == r_h:
            return l_h, root
        if l_h < r_h:
            return r_h, r_r
        return l_h,l_r
        
    
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root,0)[1]