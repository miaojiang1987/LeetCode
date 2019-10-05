# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        dist=10000000000
        closest_value=0
        while root:
            if abs(target-root.val)<dist:
                dist=abs(target-root.val)
                closest_value=root.val
            if target<root.val:
                root=root.left
            else:
                root=root.right
        
        
        return closest_value