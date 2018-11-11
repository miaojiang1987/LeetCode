class Solution:
    def permute(self, nums):
        result=[]
        if not nums or len(nums)==0:
            return result
        item=[]
        visit=[0 for i in range(len(nums))]
        self.dfs(nums,result,item,visit)        
        return result
        
        
        
    
    def dfs(self,nums,result,item,visit):
        
        if len(item)==len(nums):
            result.append(item+[])
            return
        
        for i in range(len(nums)):
            if visit[i]: continue
            num=nums[i]
            item.append(nums[i])
            visit[i]=1
            self.dfs(nums,result,item,visit)
            visit[i]=0
            item.pop()