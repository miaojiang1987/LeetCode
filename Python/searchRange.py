class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_res = self.searchLeft(nums, target)
        right_res = self.searchRight(nums, target)

        if left_res <= right_res:
            return (left_res, right_res)
        else:
            return [-1, -1]
    
    
    def searchLeft(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]: 
                low = mid + 1
            else: 
                high = mid - 1
        return low

    def searchRight(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target >= nums[mid]: 
                low = mid + 1
            else: 
                high = mid - 1
        return high
    
