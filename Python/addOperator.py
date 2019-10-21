class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        
        result=[]
        
        def dfs(start,expr,val,prev):
        
            if len(num)==start and val==target:
                result.append(expr)
                return

            for i in range(start,len(num)):
                cur_val=num[start:i+1]
                if len(cur_val) != len(str(int(cur_val))): break
                if start==0:
                    dfs(i+1,cur_val,int(cur_val),int(cur_val))
                else:
                    dfs(i+1, expr+'+'+cur_val, val+int(cur_val), int(cur_val))
                    dfs(i+1, expr+'-'+cur_val, val-int(cur_val),-int(cur_val))
                    dfs(i+1, expr+'*'+cur_val, val-prev+prev*int(cur_val), prev*int(cur_val))

        dfs(0,'',0,0)
        return result