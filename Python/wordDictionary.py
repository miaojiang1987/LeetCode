class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['END'] = ''
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(t, word):
            for idx in range(len(word)):
                w = word[idx]
                if w not in t and w != '.':
                    return False
                if w == '.':
                    return any([dfs(t[c], word[idx+1:]) for c in t])
                else:
                    t = t[w]
            return 'END' in t

        return dfs(self.trie, word)
