class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result=[]
        hashmap={}
        for c in p:
            if c in hashmap: 
                hashmap[c]+=1
            else:
                hashmap[c]=1
        match_count=0
        left=0
        
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]-=1
                if hashmap[s[i]]>=0:
                    match_count+=1
            
            while match_count==len(p):
                if i-left+1==len(p):
                    result.append(left)
                if s[left] in hashmap:
                    hashmap[s[left]]+=1
                    if hashmap[s[left]]>0:
                        match_count-=1
                left+=1
        
        return result