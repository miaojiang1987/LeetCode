# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #1->2->3->4
        if not head:
            return None
        
        dummy=ListNode(-1)
        dummy.next=head
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        head2=slow.next
        slow.next=None
        
        prev,cur,nxt=None,head2,None
        
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            
        
        cur2=head2=prev
        cur1=head1=dummy.next
        
        while cur2:
            temp1 = cur1.next
            temp2 = cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2
            
        return dummy.next
            