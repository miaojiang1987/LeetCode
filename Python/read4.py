class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        index = 0
        remain = n
        while remain > 0:
            buf4 = [0] * 4
            size = read4(buf4)
            if size == 0:
                return index
            
            for i in range(min(size, remain)):
                buf[index] = buf4[i]
                index += 1
                remain -= 1
                
        return index
