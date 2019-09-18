class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def _score(word, match):
            score = 0 
            for i in range(len(word)):
                if word[i] == match[i]:
                    score += 1
            return score
        
        wordlist.sort(key=lambda x: x[-1])
        word_set = set(range(len(wordlist)))
        while word_set:
            i = word_set.pop()
            word = wordlist[i]
            score = master.guess(word)
            word_set = {w for w in word_set if _score(wordlist[w], word) == score}