class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s)==0:
            return 0
        
        start=0
        
        longest=0
        hashmap={}
        
        for i in range(len(s)):
            
            if s[i] in hashmap:
                start=max(start,hashmap[s[i]]+1)
            longest=max(i-start+1,longest)
            hashmap[s[i]]=i
        
        
        return longest