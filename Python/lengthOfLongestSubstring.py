class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        
        hashmap={}
        start = 0
        maxLength=0
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            else:
                pre_index = hashmap[s[i]]
                start = max(pre_index + 1, start)
                hashmap[s[i]] = i
            maxLength = max(maxLength, i-start+1)
        
        return maxLength