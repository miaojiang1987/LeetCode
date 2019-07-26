class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums or len(nums)<k: 
            return -1
        total=0
        for i in range(k):
            total+=nums[i]
        result=total
        
        for i in range(k,len(nums)):
            total+=nums[i]-nums[i-k]
            result=max(total,result)
        
        return result*1.0/k