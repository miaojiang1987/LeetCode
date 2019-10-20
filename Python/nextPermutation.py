class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1,2,7,4,3,1
        #   i     j
        # 1,3,7,4,2,1
        # 1,3,1,2,4,7
        
        i=len(nums)-1
        
        while i>=1 and nums[i]<=nums[i-1]:
            i-=1
        
        i-=1
        
        j=len(nums)-1
        
        if i>=0:
            j=len(nums)-1
            
            while nums[j]<=nums[i]:
                j-=1
            
            nums[j],nums[i]=nums[i],nums[j]
        
        left=i+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        