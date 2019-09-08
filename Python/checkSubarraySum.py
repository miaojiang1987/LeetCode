class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cumSum=0
        hashmap={0:-1}
        for i in range(len(nums)):
            cumSum+=nums[i]
            mod=cumSum%k if k!=0 else cumSum
            if mod in hashmap:
                if i-hashmap[mod]>=2:
                    return True
            else:
                hashmap[mod]=i
        
        
        return False
            