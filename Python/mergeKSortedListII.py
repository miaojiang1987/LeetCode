# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists)==0:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = self.mergeTwoSortedList(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]
    
    
    
    def mergeTwoSortedList(self,node1,node2):
        dummy=ListNode(-1)
        cur=dummy
        while node1 and node2:
            if node1.val<node2.val:
                cur.next=node1
                node1=node1.next
            else:
                cur.next=node2
                node2=node2.next
            cur=cur.next
        
        if node1:
            cur.next=node1
        if node2:
            cur.next=node2
        
        return dummy.next