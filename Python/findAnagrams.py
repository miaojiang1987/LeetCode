class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(s)<len(p):
            return []
        
        hashmap={}
        
        for c in p:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1
        result=[]
        start=0
        count=0
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]-=1
                if hashmap[s[i]]>=0:
                    count+=1
            
            while count==len(p):
                if i-start+1==len(p):
                    result.append(start)
                if s[start] in hashmap:
                    hashmap[s[start]]+=1
                    if hashmap[s[start]]>0:
                        count-=1
                start+=1
        
        
        return result