class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.end=True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word,self.root,0)
    
    def dfs(self,word,cur,start):
        if start==len(word):
            return cur.end
        c=word[start]
        if c!='.':
            if c not in cur.children:
                return False
            else:
                return self.dfs(word,cur.children[c],start+1)
        else:
            for child in cur.children:
                if self.dfs(word,cur.children[child],start+1):
                    return True
        
        return False