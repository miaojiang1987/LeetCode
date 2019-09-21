class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result=[]
        if not num:
            return result
        
        def recurse(start,expr,val,prev_val):
            
           
            if start==len(num) and target==val:
                result.append(expr)
                return
            
            for i in range(start,len(num)):
                cur_val=num[start:i+1]
                if len(cur_val) != len(str(int(cur_val))): break
                if start==0:
                    recurse(i+1,cur_val,int(cur_val),int(cur_val))
                
                else:
                    recurse(i+1, expr+'+'+cur_val, val+int(cur_val), int(cur_val))
                    recurse(i+1, expr+'-'+cur_val, val-int(cur_val), -int(cur_val))   # -curr is interpreted as +(-curr)
                    recurse(i+1, expr+'*'+cur_val, val-prev_val+prev_val*int(cur_val), prev_val*int(cur_val))
                

        recurse(0,'',0,0)
        return result
