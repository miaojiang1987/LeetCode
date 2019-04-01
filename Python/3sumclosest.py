class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        distance=pow(2,32)-1
        result=0
        for t in range(len(nums)-2):
            i=t+1
            j=len(nums)-1
            
            while i<j:
                _sum=nums[t]+nums[i]+nums[j]
                
                if _sum==target:
                    return _sum
                elif _sum<target:
                    i+=1
                
                else:
                    j-=1
                
                diff=abs(_sum-target)
                if diff<distance:
                    distance=diff
                    result=_sum
                           
        
        
        return result