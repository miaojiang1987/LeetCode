class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        result=0
        numAge=[0]*121
        sumAge=[0]*121
        
        for age in ages:
            numAge[age]+=1
        
        sumAge[0]=numAge[0]
        for i in range(1,121):
            sumAge[i] = numAge[i] + sumAge[i-1]
        
        for i in range(15,121):
            count=sumAge[i]-sumAge[i//2+7]
            
            result+=count*numAge[i]-numAge[i]
        
        
        return result