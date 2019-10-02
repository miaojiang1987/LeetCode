"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head=Node(insertVal)
            head.next=head
            return head
        
        prev=head
        cur=head.next
        
        while cur!=head:
            if prev.val<=insertVal<=cur.val:
                break
            
            if prev.val > cur.val and (prev.val <= insertVal or insertVal <= cur.val):
                break
            
            prev=cur
            cur=cur.next
        
                   
        new = Node(insertVal)
        prev.next = new
        new.next = cur
        
        return head