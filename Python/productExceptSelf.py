class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        result=[0 for i in range(len(nums))]
        
        result[0]=1
   
        for i in range(1,len(nums)):
            result[i]=result[i-1]*nums[i-1]
        
        right=1
        for j in range(len(nums)-1,-1,-1):
            result[j]=result[j]*right
            right*=nums[j]
        
        return result