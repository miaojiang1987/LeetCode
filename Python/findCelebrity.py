class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=0,n-1
        while left<right:
            if knows(left,right):
                left+=1
            else:
                right-=1
        
        candidate=left
        for i in range(n):
            if (candidate!=i and knows(candidate,i)) or (not knows(i,candidate)):
                return -1
        
        return candidate