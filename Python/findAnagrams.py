class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_map={}
        for letter in p:
            p_map[letter]=p_map.get(letter,0)+1
        result=[]
        start=0
        count=0
        for i in range(len(s)):
            if s[i] in p:
                p_map[s[i]]-=1
                if p_map[s[i]]>=0:
                    count+=1
            
            while count==len(p):
                if i-start+1==len(p):
                    result.append(start)
                if s[start] in p_map:
                    p_map[s[start]] += 1
                    if p_map[s[start]] > 0:
                        count -= 1
            
                start+=1
        
        
        return result