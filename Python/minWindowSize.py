class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap={}
        start=index=0
        
        minLen=sys.maxsize
        count=0
        for char in t:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
        #print(hashmap)
        for i in range(len(s)):        
            if s[i] in hashmap:
                hashmap[s[i]]-=1  
                if hashmap[s[i]]>=0:
                    count+=1
            while count==len(t):
                if minLen>i-start+1:
                    minLen=i-start+1
                    index=start
                if s[start] in hashmap:
                    hashmap[s[start]]+=1
                    if hashmap[s[start]]>0:
                        count-=1
                start+=1
        
        if minLen==sys.maxsize:
            return ""
        
        return s[index:index+minLen]