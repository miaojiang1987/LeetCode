class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        global_max=nums[0]
        current_max=nums[0]
        
        for i in range(1,len(nums)):
            current_max=max(nums[i],current_max+nums[i])
            global_max=max(global_max,current_max)
        
        
        return max(global_max,current_max)