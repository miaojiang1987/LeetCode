 class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def modifyDistance(x, y):
            return x**2 + y**2
        
        heap = []
        for p in points:
            heapq.heappush(heap, (modifyDistance(p[0], p[1]), p))
            
        ans = []
        for _ in range(K):
            ans.append(heapq.heappop(heap)[1])
            
        return ans