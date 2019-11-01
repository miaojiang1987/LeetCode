class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort(key=lambda x:x[0])
        
        for i in range(len(intervals)-1):
            if intervals[i+1][0]<intervals[i][1]:
                return False
        
        
        return True