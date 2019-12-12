class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result=[]
        queue=[]
        queue.append((root,"first"))
        
        while queue:
            node,label=queue.pop()
            if label=='first':
                queue.append((node,'second'))
                if node.right:
                    queue.append((node.right,'first'))
                if node.left:
                    queue.append((node.left,'first'))
            else:
                result.append(node.val)
        
        
        return result