class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        if not num: return []
        res = []

        def helper(start, expr, val, prev):
            if val == target and start == len(num):
                res.append(expr)
                return
            
            for i in range(start, len(num)):
                curr = num[start: i+1]
                if len(curr) != len(str(int(curr))): break   # prevent '00','01',... treated as one number
                if start == 0:
                    helper(i+1, curr, int(curr), int(curr))
                else:
                    helper(i+1, expr+'+'+curr, val+int(curr), int(curr))
                    helper(i+1, expr+'-'+curr, val-int(curr), -int(curr))   # -curr is interpreted as +(-curr)
                    helper(i+1, expr+'*'+curr, val-prev+prev*int(curr), prev*int(curr))   # since * has precedence over + we have to roll back +prev
        
        helper(0, '', 0, 0)
        return res
