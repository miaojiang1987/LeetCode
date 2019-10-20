class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        left_count=0
        right_count=0
        
        for i in range(len(S)):
            if S[i]=='(':
                left_count+=1
            elif S[i]==')':
                if left_count>0:
                    left_count-=1
                else:
                    right_count+=1
        
        
        return left_count+right_count