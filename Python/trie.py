class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}
        self.end=False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root=self
        for c in word:
            if c not in root.trie:
                root.trie[c]=Trie()
            root=root.trie[c]
        root.end=True
        
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root=self
        for c in word:
            if c not in root.trie:
                return False
            root=root.trie[c]
        
        return root.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root=self
        for c in prefix:
            if c not in root.trie:
                return False
            root=root.trie[c]
        
        return True