# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def longest_path(root):
            if not root:
                return 0, 0
            inc, dec = 1, 1
            l_inc, l_dec = longest_path(root.left)
            r_inc, r_dec = longest_path(root.right)
            if root.left:
                if root.left.val == root.val + 1:
                    inc = max(inc, 1 + l_inc)
                if root.left.val == root.val - 1:
                    dec = max(dec, 1 + l_dec)
            if root.right:
                if root.right.val == root.val + 1:
                    inc = max(inc, 1 + r_inc)
                if root.right.val == root.val - 1:
                    dec = max(dec, 1 + r_dec)
            res[0] = max(res[0], inc + dec - 1)
            return (inc, dec)
        
        res = [0]
        longest_path(root)
        return res[0]