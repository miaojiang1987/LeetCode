class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        cur_max = float('-inf')
        for idx, num in enumerate(nums):
            if num[0] > cur_max:
                cur_max = num[0]
            heapq.heappush(heap, (num[0], idx))
            num.pop(0)
        
        res = []   
        min_range = float('inf')
        
        while heap:            
            next_num, ls_idx = heapq.heappop(heap)
            if cur_max - next_num < min_range or cur_max - next_num == min_range and next_num < res[0]:
				res = [next_num, cur_max]
				min_range = cur_max - next_num
            if nums[ls_idx]:
				heapq.heappush(heap, (nums[ls_idx][0], ls_idx))
				if nums[ls_idx][0] > cur_max:
					cur_max = nums[ls_idx][0]
				nums[ls_idx].pop(0)
            else:
                break
        
        return res