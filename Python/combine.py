class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        temp=[]
        result=[]
        self.dfs(temp,result,1,n,k)
        return result
        
    
    def dfs(self,temp,result,start,n,k):
        #print(start)
        if len(temp)==k:
            result.append(temp+[])
            return
        for i in range(start,n+1):
            temp.append(i)
            self.dfs(temp,result,i+1,n,k)
            temp.pop()