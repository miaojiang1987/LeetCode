class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns=len(s)
        nt=len(t)
        
        if ns>nt: 
            return self.isOneEditDistance(t,s)
        
        if nt-ns>2: 
            return False
        
        for i in range(ns):
            if s[i]!=t[i]:
                if ns==nt:
                    return s[i+1:]==t[i+1:]
                
                else:
                    return s[i:]==t[i+1:]
        
        
        
        return nt==ns+1