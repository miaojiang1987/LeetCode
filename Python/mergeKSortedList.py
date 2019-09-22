class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq=[]
        for l in lists:
            if l:
                heapq.heappush(pq,(l.val,l))
        
        dummy=ListNode(-1)
        cur=dummy
        while pq:
            smallest=heapq.heappop(pq)[1]
            cur.next=smallest
            cur=cur.next
            if smallest.next:
                heapq.heappush(pq, (smallest.next.val, smallest.next))
                           
        return dummy.next