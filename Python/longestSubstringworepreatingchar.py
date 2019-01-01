class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        start=0
        longest=0
        for i in range(len(s)):
            if s[i] in hashmap:
                start=max(hashmap[s[i]]+1,start)
            hashmap[s[i]]=i
            longest=max(longest,i-start+1)
        return longest