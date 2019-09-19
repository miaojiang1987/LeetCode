class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        self.prev=None
        self.head=None
        self.dfs(root)
        
        self.prev.right=self.head
        self.head.left=self.prev
        
        return self.head
    
    def dfs(self,root):
        if not root:
            return
        
        self.dfs(root.left)
        
        if not self.prev:
            self.head=root
        else:
            self.prev.right=root
            root.left=self.prev
        
        self.prev=root
        self.dfs(root.right)