class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)<=1:
            return nums
        
        partition=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                partition=i
                break
        
        if partition==-1:
            nums.reverse()
        else:
            for i in range(len(nums)-1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i],nums[partition] = nums[partition],nums[i]
                    break
            left = partition+1; right = len(nums)-1
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1; right-=1
        