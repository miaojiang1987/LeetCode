class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
               
        # 1 2 7 4 3 1
        #   i     j
        # 1 3 7 4 2 1
        # 1 3 1 2 4 7 
        
        i=len(nums)-1
        
        while i>=1 and nums[i-1]>=nums[i]:
            i-=1
        i-=1
        
        if i>=0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        l, r = i+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1