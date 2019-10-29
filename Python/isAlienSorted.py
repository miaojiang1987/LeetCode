class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if not words:
            return True
        if not order:
            return False
        
        hashmap={c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            
            for c in range(min(len(word1),len(word2))):
                if hashmap[word1[c]]>hashmap[word2[c]]:
                    return False
                elif hashmap[word1[c]]<hashmap[word2[c]]:
                    break
            
            else:
                if len(word1)>len(word2):
                    return False
        
                           
                           
        return True