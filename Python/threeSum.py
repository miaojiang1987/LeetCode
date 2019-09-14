class Solution(object):
    def threeSum(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num.sort()
        result=[]
        N=len(num)
        for i in range(N-2):
            if i>0 and num[i]==num[i-1]:
                continue
            
            j=i+1
            k=N-1
            
            while j<k:
                _sum=num[i]+num[j]+num[k]
                
                if _sum==0:
                    result.append([num[i],num[j],num[k]])
                    j+=1
                    k-=1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
                        
        return result