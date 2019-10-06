class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        _max=float('-inf')
        _min=float('inf')
        pq=[]
        
        for list_index in range(len(nums)):
            if nums[list_index][0]>_max:
                _max=nums[list_index][0]
            
            if nums[list_index][0]<_min:
                _min=nums[list_index][0]
            
            heapq.heappush(pq,(nums[list_index][0], list_index))
            nums[list_index].pop(0)
        
        min_range=_max-_min
        res = [_min, _max]
        
        while pq:
            num,index=heapq.heappop(pq)
            if _max-num<min_range or (_max-num==min_range and num<res[0]):
                res = [num, _max]
                min_range = _max - num
            
            if nums[index]:
                heapq.heappush(pq,(nums[index][0], index))
                if nums[index][0] > _max:
                    _max = nums[index][0]
                nums[index].pop(0)
            else:
                break
        
        
        return res