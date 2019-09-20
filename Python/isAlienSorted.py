class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hashmap={c:i for i,c in enumerate(order)}
        #print(hashmap)
        for i in range(0,len(words)-1):
            word1=words[i]
            word2=words[i+1]
            
            size=min(len(word1),len(word2))
            
            for j in range(size):
                if word1[j]!=word2[j]:
                    if hashmap[word1[j]]>hashmap[word2[j]]:
                        return False
                    break
        
            else:
                if len(word1)>len(word2):
                    return False
        
        
        return True