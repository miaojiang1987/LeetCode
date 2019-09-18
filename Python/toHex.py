class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num > 0:
            return self.r_hex(num)
        else:
            return self.r_hex((2**32) + num)
    
    def r_hex(self, num):    
        if num == 0:
            return ""
        hexes = "0123456789abcdef"
        return self.r_hex(num//16) + hexes[num%16]