class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cumSum=0
        hashmap={0:-1}
        
        #pre_sum[i]-pre_sum[j]=k*n
        # pre_sum[i]%k==pre_sum[j]%k
        # 2,3,4
        #pre_sum[0]=2
        #pre_sum[2]=9
        #pre_sum[2]-pre_sum[0]=7*n
        #pre_sum[2]%7=2 pre_sum[0]%7=2
        
        for i in range(len(nums)):
            cumSum+=nums[i]
            mod=cumSum%k if k!=0 else cumSum
            if mod in hashmap:
                j=hashmap[mod]
                if i-j>=2:
                    return True
            else:
                hashmap[mod]=i
        
        return False