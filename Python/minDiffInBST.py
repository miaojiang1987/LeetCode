class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans=min(self.ans,node.val-self.prev)
                self.prev=node.val
                dfs(node.right)
        
        self.prev=float('-inf')
        self.ans=float('inf')
        
        dfs(root)
        return self.ans