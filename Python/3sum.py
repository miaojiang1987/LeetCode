class Solution(object):
    def threeSum(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num.sort()
        result=[]
        N=len(num)
        
        for t in range(N-2):
            if t>0 and num[t]==num[t-1]:
                continue
            
            i=t+1
            j=N-1

            while i<j:
                _sum=num[t]+num[i]+num[j]
                
                if _sum==0:
                    result.append([num[t],num[i],num[j]])
                    i+=1
                    j-=1
                    
                    while i<j and num[i]==num[i-1]:
                        i+=1
                        
                    while i<j and num[j]==num[j+1]:
                        j-=1
                    
                elif _sum<0:
                    i+=1
                
                elif _sum>0:
                    j-=1
        
        return result