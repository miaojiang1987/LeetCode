class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0 or numRows<0:
            return None
        result=[]
        temp=[1]
        result.append(temp)
        
        for i in range(1,numRows):
            prev=temp
            temp=[0]*(i+1)
            for j in range(i+1):
                if j==0:
                    temp[j]=prev[j]
                elif j==i:
                    temp[j]=prev[j-1]
                else:
                    temp[j]=prev[j-1]+prev[j]
            result.append(temp)
        
        return result