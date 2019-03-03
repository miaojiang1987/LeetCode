class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count_1={}
        count_2={}
        for i in nums1:
            if i in count_1:
                count_1[i]+=1
            else:
                count_1[i]=1
                
        for i in nums2:
            if i in count_2:
                count_2[i]+=1
            else:
                count_2[i]=1
        
        result=[]
        
        for j in count_1:
            if j in count_2:
                m1=count_1[j]
                m2=count_2[j]
                m=min(m1,m2)
                for _ in range(m):
                    result.append(j)
        
        
        return result