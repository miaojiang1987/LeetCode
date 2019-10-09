class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(len(s)):
            result+=hashmap[s[i]]
            if i>0 and hashmap[s[i-1]]<hashmap[s[i]]:
                result-=2*hashmap[s[i-1]]
        
        
        return result