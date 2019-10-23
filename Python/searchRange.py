class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_result=self.searchLeft(nums,target)
        right_result=self.searchRight(nums,target)
        
        if left_result<=right_result:
            return [left_result,right_result]
        else:
            return [-1,-1]
    
    def searchLeft(self,nums,target):
        left=0
        right=len(nums)-1
        
        
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
            
        return left
    
    def searchRight(self,nums,target):
        left=0
        right=len(nums)-1
        
        
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
            
        return right