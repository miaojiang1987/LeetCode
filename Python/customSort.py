class Solution:
    def customSortString(self, S: str, T: str) -> str:
        
        # dic[char] will be the number of occurrences of 'char' in T.
        dic = {}
        for c in T:
            dic[c] = dic[c]+1 if c in dic else 1
            
        # Write all characters that occur in S, in the order of S.   
        res = ""
        for c in S:
            if c in dic:
                res += c*dic[c]
                
        # Write all remaining characters that don't occur in S.
        for c in dic:
            if c not in set(S):
                res += c*dic[c]
        return res