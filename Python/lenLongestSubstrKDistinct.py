class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k==0:return 0
        n=len(s)
        maxLen=1
        left=right=0
        hashmap=collections.defaultdict()
        
        for right in range(len(s)):
            hashmap[s[right]]=right
            if len(hashmap)==k+1:
                start=min(hashmap.values())
                left=start+1
                del hashmap[s[start]]
            
            maxLen=max(maxLen,right-left+1)
        
        
        return maxLen