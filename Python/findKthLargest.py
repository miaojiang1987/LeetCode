class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums)<k:
            return -1
        l=0
        r=len(nums)-1
        while l<=r:
            p=self.partition(nums,l,r)
            if p==k-1:
                return nums[p]
            elif p>k-1:
                r=p-1
            else:
                l=p+1
                
         
    
    def partition(self,nums,l,r):
        p=l
        pivot=nums[p]
        
        while l<=r:
            while l<=r and nums[l]>=pivot:
                l+=1
            while l<=r and nums[r]<=pivot:
                r-=1
            
            if l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        
        nums[r],nums[p]=nums[p],nums[r]
        return r