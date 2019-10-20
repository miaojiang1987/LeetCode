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
        if not lists:
            return None
        heap=[]
        dummy=ListNode(-1)
        cur=dummy
        for lst in lists:
            if lst:
                heapq.heappush(heap,(lst.val, lst))
        
        while heap:
            node=heapq.heappop(heap)[1]
            cur.next=ListNode(node.val)
            cur=cur.next
            if node.next:
                heapq.heappush(heap,(node.next.val,node.next))
        
        
        return dummy.next