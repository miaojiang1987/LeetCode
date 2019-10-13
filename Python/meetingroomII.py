class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        result=1
        intervals.sort()
        
        pq=[]
        heapq.heappush(pq,intervals[0][1])
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<pq[0]:
                result+=1
            else:
                heapq.heappop(pq)
            heapq.heappush(pq,intervals[i][1])
        
        return result