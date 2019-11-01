class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        return self.dfs(self.root, word, 0)
        
    def dfs(self, node, word, start):
        if start == len(word):
            return node.end
        c = word[start]
        if c != '.':
            if c not in node.children:
                return False
            return self.dfs(node.children[c], word, start+1)     
        else:
            for child in node.children:
                if self.dfs(node.children[child], word, start+1):
                    return True
            return False
        