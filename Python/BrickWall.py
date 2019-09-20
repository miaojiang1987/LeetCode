class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hashmap={}
        result=0
        for w in wall:
            points=0
            for i in range(len(w)-1):
                points+=w[i]
                if points in hashmap:
                    hashmap[points]+=1
                else:
                    hashmap[points]=1
                result=max(hashmap[points],result)
                
        
        return len(wall)-result