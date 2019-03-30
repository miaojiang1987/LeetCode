class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        if not root:
            return result
        
        queue=[root]
        
        while queue:
            temp=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                temp.append(node.val)
            
            result.append(max(temp))
        
        return result