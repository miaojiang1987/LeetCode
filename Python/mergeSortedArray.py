class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy=nums1[:m]
        
        
        p1=0
        p2=0
        
        i=0
        
        while p1<m and p2<n:
            if nums1_copy[p1]<nums2[p2]:
                nums1[i]=nums1_copy[p1]
                p1+=1
            else:
                nums1[i]=nums2[p2]
                p2+=1
            i+=1
        
        if p1<m:
            nums1[i:m+n]=nums1_copy[p1:]
        else:
            nums1[i:m+n]=nums2[p2:]