class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        result=0
        pre_sum=0
        hashmap={0:1}
        for i in range(len(nums)):
            pre_sum+=nums[i]
            if pre_sum-k in hashmap:
                result+=hashmap[pre_sum-k]
            
            if pre_sum not in hashmap:
                hashmap[pre_sum]=1
            else:
                hashmap[pre_sum]+=1
        
        
        
        
        return result