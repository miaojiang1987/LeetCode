class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap=[]
        for p in points:
            dist=p[0]**2+p[1]**2
            heapq.heappush(heap,(-dist,p))
            if len(heap)>K:
                heapq.heappop(heap)
        
        result=[]
        for i in range(len(heap)):
            result.append(heapq.heappop(heap)[1])
        
        
        return result[::-1]