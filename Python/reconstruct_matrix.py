class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        upper_row=[0]*len(colsum)
        lower_row=[0]*len(colsum)

        if (upper+lower)!=sum(colsum):
            
            return result
        
        for i in range(len(colsum)):
            if upper<0 or lower<0:
                return []
            if colsum[i]==2:
                upper_row[i]=lower_row[i]=1
                upper-=1
                lower-=1
            elif colsum[i]==0:
                upper_row[i]=lower_row[i]=0
            
        for i in range(len(colsum)):
            if colsum[i]==1:
                if upper>0 and lower>0:
                    lower_row[i]=1
                    lower-=1
                else:
                    upper_row[i]=1
                    upper-=1        
        
        result.append(upper_row)
        result.append(lower_row)
        return result