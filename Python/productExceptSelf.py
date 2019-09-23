class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        
        result=[1]*n
        
        #[1,2,3,4]
        #[24,12,4,1]
        for i in range(n-2,-1,-1):
            result[i]=result[i+1]*nums[i+1]
        
        left_product=1
        
        for i in range(len(nums)):
            result[i]=left_product*result[i]
            left_product*=nums[i]
        
        return result