class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        left=0
        right=len(lists)-1
        while right>0:
            if left<right:
                lists[left]=self.mergeTwoSortedList(lists[left],lists[right])
                left+=1
                right-=1
            else:
                left = 0
        return lists[0]
    
    
    def mergeTwoSortedList(self,l1,l2):
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            if l1.val>l2.val:
                cur.next=l2
                l2=l2.next
                cur=cur.next
            else:
                cur.next=l1
                l1=l1.next
                cur=cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return dummy.next