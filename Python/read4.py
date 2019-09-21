class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        c, m, buf4 = 0, 4, [0] * 4
        while c < n and m == 4:
            m = read4(buf4)
            buf[c:m] = buf4[:m]
            c += m
        return min(c, n)