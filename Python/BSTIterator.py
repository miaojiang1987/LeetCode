class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def hasNext(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return len(self.stack)!=0
        

    def next(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        node=self.stack.pop()
        cur=node.right
        while cur:
            self.stack.append(cur)
            cur=cur.left
        return node.val