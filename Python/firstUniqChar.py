class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        if not s:
            return -1
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=1
            else:
                hashmap[s[i]]+=1
        
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        
        return -1