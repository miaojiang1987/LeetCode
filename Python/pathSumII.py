# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result=[]
        temp=[]
        
        self.dfs(root,result,temp,sum)
        
        return result
    
    def dfs(self,root,result,temp,sum):
        if not root:
            return 
        
        #if root.val>sum:
        #    return
        
        if not root.left and not root.right:
            if sum==root.val:
                result.append(temp+[root.val])
        
        else:
            self.dfs(root.left,result,temp+[root.val],sum-root.val)
            self.dfs(root.right,result,temp+[root.val],sum-root.val)