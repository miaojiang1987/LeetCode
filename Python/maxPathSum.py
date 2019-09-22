class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result=float('-inf')
        self.dfs(root)
        return self.result
    
    def dfs(self,root):
        if not root:
            return 0
        
        left_result=max(self.dfs(root.left),0)
           
        right_result=max(self.dfs(root.right),0)
        
        self.result=max(self.result,root.val+left_result+right_result)
        
        return max(left_result,right_result)+root.val