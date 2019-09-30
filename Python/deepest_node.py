# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return self.dfs(root)[1]
        
        
    def dfs(self, root):
        
        if not root:
            return (-1, None)
        left_depth, left_res = self.dfs(root.left)
        right_depth, right_res = self.dfs(root.right)
        if left_depth == right_depth:
            return (left_depth+1, root)
        elif left_depth > right_depth:
            return (left_depth+1, left_res)
        else:
            return (right_depth+1, right_res)
        