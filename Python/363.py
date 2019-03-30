# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        if not root:
            return result
        self.hashmap=collections.defaultdict(list)
        self.maxDepth=0
        self.dfs(root)
        for depth in range(1,self.maxDepth+1):
            result.append(self.hashmap[depth])
        
        return result
    
    
    def dfs(self,root):
        if not root:
            return 0
        
        depth=max(self.dfs(root.left),self.dfs(root.right))+1
        self.maxDepth=max(depth,self.maxDepth)
        self.hashmap[depth].append(root.val)
        
        return depth