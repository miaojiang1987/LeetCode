class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        current=head
        prev=None
        
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
        return prev