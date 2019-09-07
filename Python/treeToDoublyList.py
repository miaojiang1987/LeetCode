class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        prev,cur=None,root
        stack=[]
        head=None
        
        while cur:
            stack.append(cur)
            cur=cur.left
        
        while stack:
            cur=stack.pop()
            if not prev:
                head=cur
            else:
                prev.right=cur
                cur.left=prev
            prev=cur
            cur=cur.right
            while cur:
                stack.append(cur)
                cur=cur.left
        
        if prev and head:
            prev.right=head
            head.left=prev
        
        return head
            