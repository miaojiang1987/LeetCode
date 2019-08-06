class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if not words:
            return False
        order_index={c:i for i,c in enumerate(order)}
        
        if len(words)==1: return True
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            
            for k in range(min(len(word1),len(word2))):
                if word1[k]!=word2[k]:
                    if order_index[word1[k]]>order_index[word2[k]]:
                        return False
                    break
            else:
                if len(word1)>len(word2):
                    return False
        
        return True