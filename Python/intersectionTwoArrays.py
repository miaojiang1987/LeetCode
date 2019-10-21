class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return None
        
        hashset=set()
        result=[]
        
        for num in nums1:
            if num not in hashset:
                hashset.add(num)
        
        for num in nums2:
            if num in hashset:
                result.append(num)
                hashset.remove(num)
        
        return result