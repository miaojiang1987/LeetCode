class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxLen=1
        curLen=1
        if len(nums)==1:
            return 1
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curLen+=1
                maxLen=max(maxLen,curLen)
            
            else:
                curLen=1
        
        
        return maxLen