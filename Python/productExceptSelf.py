class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        
        #[1,2,3,4]
        # From left:[1,1,2,6]
        # From right:[1,1,2,6] (R=4), [1,1,8,6] (R=12) [1,12,8,6] (R=24)
        answer=[1 for i in range(len(nums))]
        answer[0]=1

        for i in range(1,len(nums)):
            answer[i]=answer[i-1]*nums[i-1]
      
        R=1
        
        for i in range(len(nums)-1,-1,-1):
            answer[i]=answer[i]*R
            R*=nums[i]
        
        
        return answer