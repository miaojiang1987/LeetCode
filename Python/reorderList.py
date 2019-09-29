# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return None
        dummy=ListNode(-1)
        dummy.next=head
        fast = slow = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        slow.next = None
        
        prev,cur,next=None,head2,None
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        head2=prev
        
        #1,2,3
        #5,4
        #1,5,2,4,3
        cur1, cur2 = head1, head2
        while cur2:
            temp1=cur1.next
            temp2=cur2.next
            cur1.next=cur2
            cur2.next=temp1
            cur1=temp1
            cur2=temp2
        
        return dummy.next
            