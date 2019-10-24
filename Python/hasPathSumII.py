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
        result=[]
        temp=[]
        self.dfs(result,temp,root,sum)
        return result
    
    
    def dfs(self,result,temp,root,target):
        if not root:
            return
        
        if root.val==target and not root.left and not root.right:
            result.append(temp+[root.val]) 
        else:
            self.dfs(result,temp+[root.val],root.left,target-root.val)
            self.dfs(result,temp+[root.val],root.right,target-root.val)
        