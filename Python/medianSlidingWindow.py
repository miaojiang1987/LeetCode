import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        k = k if len(nums) > k else len(nums)
        aux = sorted(nums[:k])
        ans = []
        for i in range(k, len(nums)):
            # print(aux)
            if  k % 2 == 0:
                ans.append((aux[k//2-1] + aux[k//2]) / 2.0)
            else:
                ans.append(aux[k//2])
        
            bisect.insort(aux, nums[i])
            aux.pop(bisect.bisect(aux, nums[i-k])-1)
            
        if  k % 2 == 0:
            ans.append((aux[k//2-1] + aux[k//2]) / 2.0)
        else:
            ans.append(aux[k//2])
        return ans