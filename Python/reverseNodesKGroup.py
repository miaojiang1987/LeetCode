# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        cur = head
        
        while cur:
            # lead pointer and follow pointer, fast forward the lead pointer by k
            fast = slow = cur
            for _ in range(k-1):
                if not fast.next:
                    return dummy.next
                fast = fast.next
                
            # bookmark start of next loop
            cur = fast.next
            res = self.reverse(slow, fast)
            prev.next = res[0]
            slow.next = cur
            prev = res[1]
            
        return dummy.next
        
    def reverse(self, start, end):
        """Reverse a list until we get to node given by 'end'."""
        prev, cur, next = None, start, None
        while prev != end:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return [end, start]