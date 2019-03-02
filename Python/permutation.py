class Solution:
    def permute(self, nums):
        result=[]
        if not nums or len(nums)==0:
            return result
        
        visited=[0 for i in range(len(nums))]
        temp=[]
        
        self.dfs(nums,temp,result,visited)
        
        return result
    
    def dfs(self,nums,temp,result,visited):
        if len(temp)==len(nums):
            result.append(temp+[])
            return 
        
        for i in range(len(nums)):
            if visited[i]: continue
            temp.append(nums[i])
            visited[i]=1
            self.dfs(nums,temp,result,visited)
            temp.pop()
            visited[i]=0