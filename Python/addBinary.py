class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        if m < n:
            a = "0"*(n-m) + a
        elif m > n:
            b = "0"*(m-n) + b
            
        res = ""
        length = max(m, n)
        i = length - 1
        j = length - 1
   
        carry = 0
        while i >= 0 and j >= 0:
            val = carry + int(a[i]) + int(b[i])
            i -= 1
            j -= 1
            digit = val % 2
            carry = val // 2
            res = str(digit) + res
            
        if carry == 1:
            res = "1" + res
            
        return res