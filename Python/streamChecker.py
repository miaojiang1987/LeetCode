from collections import defaultdict
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            level = self.trie
            for c in w[::-1]:
                if c not in level:
                    level[c] = {}
                level = level[c]
            level['#'] = 1
        self.letters = ''
        self.max_len = len(max(words, key = len))
        
    def query(self, letter: str) -> bool:
        self.letters = letter + self.letters
        tmp = self.letters[:self.max_len]
        level = self.trie
            
        for c in tmp:
            if c in level:
                level = level[c]
                if '#' in level:
                    return True
            else:
                return False