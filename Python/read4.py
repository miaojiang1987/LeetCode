class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        remain=n
        index=0
        
        while remain>0:
            buf4=['']*4
            size=read4(buf4)
            if size==0:
                return index
            
            for i in range(min(size,remain)):
                buf[index] = buf4[i]
                remain -= 1
                index += 1
        
        
        return index