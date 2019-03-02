class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue=[root]
        result=0
        
        while queue:
            result+=1
            for i in range(len(queue)):
                node=queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)