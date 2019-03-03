class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i,j=0,len(s)-1
        for k in range(len(s)/2):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1