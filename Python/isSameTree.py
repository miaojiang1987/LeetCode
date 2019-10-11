# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if not q or not p:
            return False
        queue=[]
        queue.append((p,q))
        
        while queue:
            node1,node2=queue.pop(0)
            if (node1 and not node2) or (not node1 and node2):
                return False
            
            if node1 and node2:
                if node1.val!=node2.val:
                    return False
            if node1:
                queue.append((node1.left,node2.left))
                queue.append((node1.right,node2.right))
        
        
        return True