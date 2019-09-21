class Solution(object):
    def __init__(self):
        self.buf4=[""]*4
        self.buf_index=0
        self.buf_size=0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_index=0
        
        while buf_index<n:
            while buf_index<n and self.buf_index<self.buf_size:
                buf[buf_index]=self.buf4[self.buf_index]
                buf_index+=1
                self.buf_index+=1
            
            if self.buf_index==self.buf_size:
                self.buf_index=0
                self.buf_size=read4(self.buf4)
            
            if self.buf_size==0:
                break
        
        return buf_index