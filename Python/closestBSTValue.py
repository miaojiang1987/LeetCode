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
        min_dist=float('inf')
        min_val=0
        while root:
            dist=abs(root.val-target)
            if dist<min_dist:
                min_val=root.val
                min_dist=dist
            
            if target>root.val:
                root=root.right
            else:
                root=root.left
        
        
        return min_val