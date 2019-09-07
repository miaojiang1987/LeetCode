   class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        
        res=[1]*n
        
        #[1,2,3,4] -> res=[24,12,4,1]
        for i in range(n-2,-1,-1):
            res[i]=res[i+1]*nums[i+1]
        
        leftproduct=1
        #res=[24,12,4*2,6*1]
        for i in range(n):
            res[i]*=leftproduct
            leftproduct*=nums[i]
        
        return res