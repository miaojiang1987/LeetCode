class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        best, rolling_sum = 0, 0
        lut = {0: -1}
        for j, i in enumerate(nums):
            rolling_sum += i
            if (rolling_sum - k) in lut:
                best = max(best, j - lut[rolling_sum - k])
            if rolling_sum not in lut: lut[rolling_sum] = j
        return best