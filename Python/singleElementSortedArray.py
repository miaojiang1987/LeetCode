class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        The logic here is if mid is an odd index then:
         if nums[mid-1] is equal to nums[mid] then single element is after mid else it is before mid
        if mid is even then if nums[mid] == nums[mid+1] then then single element is after mid
        else it is before mid
        """
        start = 0
        l = len(nums)
        end = len(nums) - 1
        while start <=end:
            mid = (start + end)//2
            if mid<l-1:
                if nums[mid-1] != nums[mid] and nums[mid+1] !=nums[mid]:
                    return nums[mid]
            if mid % 2 == 1:
                if nums[mid-1] == nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if mid < l -1 and  nums[mid] == nums[mid+1]:
                    start = mid + 1
                else:
                    end = mid -1
        return nums[mid]