class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idxs = []
        for i, num in enumerate(self.nums):
            if num == target:
                idxs.append(i)
        return idxs[random.randint(0, len(idxs) - 1)]