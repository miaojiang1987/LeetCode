class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        
        res = 0
        mask = 1
        for i in range(32):
            cnt = 0
            for j in range(N):
                if mask & nums[j]:
                    cnt += 1
            res += cnt * (N-cnt)
            mask <<= 1
        return res