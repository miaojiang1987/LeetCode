class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap={}
        result=[]
        if not nums1 or not nums2:
            return result
        
        for i in range(len(nums1)):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]]=1
            else:
                hashmap[nums1[i]]+=1
        
        
        for i in range(len(nums2)):
            if nums2[i] in hashmap and hashmap[nums2[i]]>0:
                hashmap[nums2[i]]-=1
                result.append(nums2[i])
        
        
        return result