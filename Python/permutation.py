class Solution:
    def permute(self, nums):
        result=[]
        
        if not nums or len(nums)==0:
            return 0
        
        temp=[]
        visited=[0 for i in range(len(nums))]
        
        self.dfs(nums,result,temp,visited)
        
        return result
    
    def dfs(self,nums,result,temp,visited):
        if len(temp)==len(nums):
            result.append(temp+[])
            return
        
        for i in range(len(nums)):
            if visited[i]: continue
            temp.append(nums[i])
            visited[i]=1
            self.dfs(nums,result,temp,visited)
            temp.pop()
            visited[i]=0