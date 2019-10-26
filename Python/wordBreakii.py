class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        tokenDict = {}
        def dfs(s):
            ans = []
            if s in wordDict:
                ans.append(s)
            for x in range(len(s) - 1):
                prefix, suffix = s[:x + 1], s[x + 1:]
                if prefix not in wordDict:
                    continue
                rest = []
                if suffix in tokenDict:
                    rest = tokenDict[suffix]
                else:
                    rest = dfs(suffix)
                for n in rest:
                    ans.append(prefix + ' ' + n)
            tokenDict[s] = ans
            return ans
        return dfs(s)