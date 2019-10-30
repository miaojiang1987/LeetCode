class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=[]
        result=[]

        zigzag=False
        
        if not root:
            return result
        
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
            if zigzag:
                temp.reverse()
                zigzag=False
            else:
                zigzag=True
            result.append(temp)
        
        return result
                