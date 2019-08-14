class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head = None
        cur = root
        stack = []
        prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev == None:
                head = cur
            else:
                prev.right = cur
                cur.left = prev
            prev = cur
            cur = cur.right
        if prev and head:
            prev.right = head
            head.left = prev
        return head