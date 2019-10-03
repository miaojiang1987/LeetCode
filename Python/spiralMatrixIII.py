class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res=[[r0,c0]]
        if R*C==1:
            return res
        
        cur=0
        step=0
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        
        
        while len(res)<R*C:
            if cur==0 or cur==2:
                step+=1
            
            for _ in range(step):
                r0 += directions[cur][0]
                c0 += directions[cur][1]
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    res.append([r0, c0])
            cur = (cur+1) % 4
        
        return res
            