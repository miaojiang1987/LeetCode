class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        if not root:
            return result
        
        queue=[]
        queue.append(root)
        
        while queue:
            temp=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            
            result.append(temp+[])
        
        result.reverse()
        
        return result