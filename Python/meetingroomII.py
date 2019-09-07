class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals or len(intervals)==0:
            return 0
        
        result=1
        pq=[]
        intervals.sort()
        heapq.heappush(pq,intervals[0][1])
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<pq[0]:
                result+=1
                heapq.heappush(pq,intervals[i][1])
            else:
                heapq.heappop(pq)
                heapq.heappush(pq,intervals[i][1])
            
        
        return result