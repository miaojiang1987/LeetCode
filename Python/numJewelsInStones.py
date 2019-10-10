class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J or not S:
            return 0
        
        jewelset=set()
        
        for j in J:
            jewelset.add(j)
        
        result=0
        for s in S:
            if s in jewelset:
                result+=1
        
        
        return result