class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J or not S:
            return 0
        result=0
        hashmap={}
        for character in S:
            if character not in hashmap:
                hashmap[character]=1
            else:
                hashmap[character]+=1
        
        for jewel in J:
            if jewel in S:
                result+=hashmap[jewel]
        
        return result