class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A or len(A)==0:
            return []
        
        word=A[0]
        counter=collections.Counter(word)    
        
        
        
        for i in range(1,len(A)):
            word=A[i]
            new_counter=collections.Counter(word)
            final_counter=collections.Counter(counter)
            for element in counter:
                if element not in new_counter:
                    del final_counter[element]
                else:
                    final_counter[element]=min(counter[element],new_counter[element])
            counter=final_counter
        
        return list(counter.elements())