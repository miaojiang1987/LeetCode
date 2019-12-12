class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue=[]
        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                node=queue.pop()
                node.left,node.right=node.right,node.left
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        
        return root