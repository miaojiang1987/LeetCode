class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap=[]
        for point in points:
            dist=self.distance(point)
            heapq.heappush(heap,(-dist,point))
            
            if len(heap) > K:
                heapq.heappop(heap)
        result=[]
    
        while heap:
            result.append(heapq.heappop(heap)[1])
            
        return result
        
    
    def distance(self,p):
        return p[0]**2+p[1]**2