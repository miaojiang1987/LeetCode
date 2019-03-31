class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        elif root.children==[]:
            return 1
        else:
            height=[self.maxDepth(child) for child in root.children]
            return max(height)+1