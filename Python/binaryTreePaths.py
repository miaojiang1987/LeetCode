# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result=[]
        if not root:
            return result
        
        self.dfs(root,result,'')
        
        return result
    
    def dfs(self,root,result,temp):
        temp+=str(root.val)
        if not root.left and not root.right:
            result.append(temp)
            return
        if root.left:
            self.dfs(root.left,result,temp+"->")
        if root.right:
            self.dfs(root.right,result,temp+"->")