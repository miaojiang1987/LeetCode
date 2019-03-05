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
        path=[]
        result=[]
        if not root:
            return result
        else:
            path=(str)(root.val)
            self.dfs(root,result,path)
        return result
    
    def dfs(self,root,result,path):
        if not root.left and not root.right:
            result.append(path)
            return
        
        if root.left:
            self.dfs(root.left,result,path+'->'+(str)(root.left.val))
        if root.right:
            self.dfs(root.right,result,path+'->'+(str)(root.right.val))