class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort()
        
        for i in range(1,len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                return False
        
        return True