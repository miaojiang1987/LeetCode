class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return None
        result=[]
        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            if not result or result[-1][1]<interval[0]:
                result.append(interval)
            
            else:
                result[-1][1]=max(result[-1][1],interval[1])
        
        
        return result