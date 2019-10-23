class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        N=len(nums)
        for i in range(N-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j=i+1
            k=N-1
            
            while j<k:
                _sum=nums[i]+nums[j]+nums[k]
                
                if _sum==0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
                        
        return result