class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        
        start=0
        
        for cur in range(len(nums)):
            if nums[cur]!=0:
                nums[start]=nums[cur]
                start+=1
        
        while start<len(nums):
            nums[start]=0
            start+=1
        
        return nums