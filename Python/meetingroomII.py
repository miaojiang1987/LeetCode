class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[0])
        
        pq=[]
        room=1
        heapq.heappush(pq,intervals[0][1])
        
        for i in range(1,len(intervals)):
            if pq[0]>intervals[i][0]:
                room+=1
            else:
                heapq.heappop(pq)
            
            heapq.heappush(pq,intervals[i][1])
        
        return room