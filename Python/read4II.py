class Solution(object):
    def __init__(self):
        self.buf=['']*4
        self.index=0
        self.buf_size=0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        index=0
        
        while index<n:
            while index<n and self.index<self.buf_size:
                buf[index]=self.buf[self.index]
                index+=1
                self.index+=1
            
            if self.index==self.buf_size:
                self.buf_size=read4(self.buf)
                self.index = 0
            
            if self.buf_size == 0:
                break
        
        return index