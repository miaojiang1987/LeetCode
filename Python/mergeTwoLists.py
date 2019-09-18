class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            if l1.val>l2.val:
                cur.next=l2
                l2=l2.next
            else:
                cur.next=l1
                l1=l1.next
            cur=cur.next
        if l1:
            while l1:
                cur.next=l1
                l1=l1.next
                cur=cur.next
        if l2:
            while l2:
                cur.next=l2
                l2=l2.next
                cur=cur.next
        
        return dummy.next