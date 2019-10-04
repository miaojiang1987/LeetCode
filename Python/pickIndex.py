class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        pre_sum=0
        self.sum_index=[]
        for i in range(len(w)):
            pre_sum+=w[i]
            self.sum_index.append(pre_sum)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        num=random.randint(1,self.sum_index[-1])
        l,r=0,len(self.sum_index)
        while l<=r:
            mid=l+(r-l)//2
            if self.sum_index[mid]==num:
                return mid
            
            elif num<self.sum_index[mid]:
                r=mid-1
            
            else:
                l=mid+1
        
        return l