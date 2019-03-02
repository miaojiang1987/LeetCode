"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result=[]
        if not root:
            return result
        
        queue=[]
        queue.append(root)
        
        while queue:
            temp=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                for child in node.children:
                    queue.append(child)
                temp.append(node.val)