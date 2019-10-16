class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        presum=0
        hashmap={0:1}
		
        
        for i in range(len(nums)):
            presum+=nums[i]
            if presum-k in hashmap:
                result+=hashmap[presum-k]
            if presum in hashmap:
                hashmap[presum]+=1
            else:
                hashmap[presum]=1
        
        
        return result