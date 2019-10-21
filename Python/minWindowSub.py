class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s)<len(t):
            return ""
        
        hashmap={}
        
        for c in t:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1
        
        count=0
        minLen=len(s)+1
        start=index=0
        
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]-=1
                if hashmap[s[i]]>=0:
                    count+=1
            
            
            while count==len(t):
                if i-start+1<minLen:
                    minLen=i-start+1
                    index=start
                    
                if s[start] in hashmap:
                    hashmap[s[start]]+=1
                    if hashmap[s[start]]>0:
                        count-=1
                start+=1
            
        if minLen==len(s)+1:
            return ""
        
        
        return s[index:index+minLen]       