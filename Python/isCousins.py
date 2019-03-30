class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        
        queue=[root]
        while queue:
            values=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                
                if node.left and node.right:
                    if (node.left.val==x and node.right.val==y) or (node.left.val==y and node.right.val==x):
                        return False
                
                if node.left:
                    queue.append(node.left)
                    values.append(node.left.val)
                
                if node.right:
                    queue.append(node.right)
                    values.append(node.right.val)
                
            if x in values and y in values:
                return True
            
            if x in values or y in values:
                return False
                
        
                
        return False