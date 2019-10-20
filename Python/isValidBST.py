# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack=[]
        while root:
            stack.append(root)
            root=root.left
        
        prev=None
        
        while stack:
            cur=stack.pop()
            if prev and cur.val<=prev.val:
                return False
            prev=cur
            cur=cur.right
            while cur:
                stack.append(cur)
                cur=cur.left
        
        
        return True