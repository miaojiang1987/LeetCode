class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        
        hashmap={0:-1}
        pre_sum=0
        
        for i in range(len(nums)):
            pre_sum+=nums[i]
            mod=pre_sum%k if k!=0 else pre_sum
            if mod in hashmap:
                j=hashmap[mod]
                if i-j>=2:
                    return True
            else:
                hashmap[mod]=i
        
        return False