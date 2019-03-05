class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result=[]
        stack=[]
        if not root:
            return result
        
        stack.append(root)
        
        while stack:
            node=stack.pop()
            result.append(node.val)
            node.children.reverse()
            for child in node.children:
                stack.append(child)
                
        
        
        return result