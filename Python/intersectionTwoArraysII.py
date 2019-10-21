class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return None
        result=[]
        hashmap={}
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        for num in nums1:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        
        for num in nums2:
            if num in hashmap:
                if hashmap[num]>0:
                    result.append(num)
                    hashmap[num]-=1
        
        
        return result