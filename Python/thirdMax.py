class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1: return nums[0]
        #if len(nums)==2: return max(nums)
        
        max_three=[]
        for i in range(len(nums)):
            if len(max_three)<3:
                if nums[i] not in max_three:
                    max_three.append(nums[i])
                    if len(max_three)==3:
                        max_three.sort()
            else:
                if nums[i] not in max_three and nums[i]>max_three[0]:
                    max_three[0]=nums[i]
                    max_three.sort()
        
      
        if len(max_three)<3: return max(max_three)
        return max_three[0]