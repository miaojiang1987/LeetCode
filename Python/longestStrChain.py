class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """


        if not words:
            return 0
        
        words = sorted(words, key=len)
        dp_dict = {}
        res = 0
        for word in words:
            max_prev = 0
            for i in range(len(word)):
                sub_word = word[:i]+word[i+1:]
                if sub_word in dp_dict:
                    max_prev = max(max_prev,dp_dict[sub_word])
            dp_dict[word]=max_prev+1
            res = max(res,max_prev+1)
        return res