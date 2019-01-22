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
        
        currentLevel=collections.deque()
        nextLevel=collections.deque()
        
        currentLevel.append(root)
        
        while currentLevel:
            node=currentLevel.popleft()
            if node:
                node.left,node.right = node.right,node.left
                nextLevel.append(node.left)
                nextLevel.append(node.right)
            
            if not currentLevel:
                currentLevel,nextLevel=nextLevel,currentLevel
        
        
        return root