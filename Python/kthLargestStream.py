class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
