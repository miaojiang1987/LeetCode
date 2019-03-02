"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        queue=[root]
        result=0
        
        while queue:
            result+=1
            for i in range(len(queue)):
                node=queue.pop(0)
                if node.children:
                    for child in node.children:
                        queue.append(child)