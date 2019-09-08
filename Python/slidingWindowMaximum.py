class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque, r = collections.deque(), []
        for i, num in enumerate(nums):
            while deque and deque[0][1] <= i - k:
                deque.popleft()

            while deque and num > deque[-1][0]:
                deque.pop()

            deque.append([num, i])

            if i >= k - 1:
                r.append(deque[0][0])
        return r
