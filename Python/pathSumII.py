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
        temp=[]
        result=[]
        self.dfs(root,sum,temp,result)        
        return result
    
    def dfs(self,root,sum,temp,result):
        if not root: return
        
        
        if not root.left and not root.right:
            if root.val==sum:
                result.append(temp+[root.val])
        else:
           
            self.dfs(root.left,sum-root.val,temp+[root.val],result)
            self.dfs(root.right,sum-root.val,temp+[root.val],result)