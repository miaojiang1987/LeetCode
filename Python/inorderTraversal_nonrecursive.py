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
        if not root:
            return result
        
        stack=[]
        
        while root:
            stack.append(root)
            root=root.left
            
        while stack:
            node=stack.pop()
            result.append(node.val)
            node=node.right
            while node:
                stack.append(node)
                node=node.left
        
        return result