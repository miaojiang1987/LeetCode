# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy=ListNode(-1)
        dummy.next=head
        
        prev=dummy
        cur=head
        
        while cur:
            slow=fast=cur
            for _ in range(k-1):
                if not fast.next:
                    return dummy.next
                fast=fast.next
            cur=fast.next
            res=self.reverse(slow,fast)
            prev.next=res[0]
            slow.next=cur
            prev=res[1]
        
        
        return dummy.next
        
              
    # 1->2->3
    # 1<-2<-3
    def reverse(self,start,end):
        prev,cur,next=None,start,None        
        while prev!=end:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        
        return [end,start]