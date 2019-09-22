class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        startPoint=[interval[0] for interval in intervals]
        startPoint.sort()
        endPoint=[interval[1] for interval in intervals]
        endPoint.sort()
        
     
        result=0
        endtime=0
        
        for i in range(len(intervals)):
            if startPoint[i]<endPoint[endtime]:
                result+=1
            else:
                endtime+=1
        
        return result