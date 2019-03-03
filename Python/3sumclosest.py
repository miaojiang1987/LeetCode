class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result=0
        distance=pow(2,32)-1
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                _sum=nums[i]+nums[k]+nums[j]
                if _sum==target:
                    return _sum
                elif _sum>target:
                    k-=1
                else:
                    j+=1
                
                diff=abs(_sum-target)
                if diff<distance:
                    distance=diff
                    result=_sum
        
        return result