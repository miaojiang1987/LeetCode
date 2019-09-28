class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        if not nums1 or not nums2:
            return result
        hashset=set()
        
        for i in range(len(nums1)):
            if nums1[i] not in hashset:
                hashset.add(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] in hashset:
                result.append(nums2[i])
                hashset.remove(nums2[i])
        
        
        return result