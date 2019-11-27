class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return None
        
        result=[]
        hashmap={}
        
        for string in strs:
            key=''.join(sorted(string))
            if key in hashmap:
                hashmap[key].append(string)
            
            else:
                hashmap[key]=[string]
            
        
        return hashmap.values()