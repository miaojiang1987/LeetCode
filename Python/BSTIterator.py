class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.stack:
            node=self.stack.pop()
            cur=node.right
            while cur:
                self.stack.append(cur)
                cur=cur.left
            return node.val
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack)>0

