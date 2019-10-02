# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes=[(root,1)]
        i=0
        
        while i<len(nodes):
            node,v=nodes[i]
            i+=1
            if node:
                nodes.append((node.left,2*v))
                nodes.append((node.right,2*v+1))
        
        
        return nodes[-1][1]==len(nodes)