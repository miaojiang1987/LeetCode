# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        current_level=collections.deque()
        next_level=collections.deque()
        
        current_level.append(root)
        while current_level:
            node=current_level.popleft()
            if node:
                node.left,node.right=node.right,node.left
                next_level.append(node.left)
                next_level.append(node.right)
            if not current_level:
                current_level=next_level
        
        
        return root