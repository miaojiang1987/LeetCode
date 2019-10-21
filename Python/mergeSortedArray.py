class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 and not nums2:
            return None
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        index_1=m-1
        index_2=n-1
        index=m+n-1
        
        while index_1>=0 and index_2>=0:
            if nums1[index_1]>nums2[index_2]:
                nums1[index]=nums1[index_1]
                index_1-=1
            else:
                nums1[index]=nums2[index_2]
                index_2-=1
            
            index-=1
        
        while index_2>=0:
            nums1[index] = nums2[index_2]
            index_2-= 1
            index -= 1