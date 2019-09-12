class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        prev=None
        stack=[]
        
        while root:
            stack.append(root)
            root=root.left
        
        while stack:
            cur=stack.pop()
            if prev and prev.val >= cur.val:
                return False
            prev=cur
            cur=cur.right
            while cur:
                stack.append(cur)
                cur=cur.left
        
        
        return True